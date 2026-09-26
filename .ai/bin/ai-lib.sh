#!/usr/bin/env bash
# .ai/bin/ai-lib.sh — shared functions for the .ai/bin/ai-* wrappers.
# Not a standalone script: `source "$(dirname "${BASH_SOURCE[0]}")/ai-lib.sh"`.
#
# GOTCHA (verified 2026-09-11): macOS ships bash 3.2 by default (GPL licensing;
# no newer bash on this machine) and never installs a newer one via brew unless
# asked. Bash 3.2 has the classic "unbound variable" bug on `"${arr[@]}"` when
# `arr` is empty AND `set -u` is active. Any possibly-empty array expansion in
# these scripts MUST use `"${arr[@]+"${arr[@]}"}"`, not `"${arr[@]}"`. `"$@"`
# is exempt (positional params are a special case bash 3.2 handles correctly).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$SCRIPT_DIR/../config.sh"

ai_log()  { printf '[.ai] %s\n' "$*" >&2; }
ai_warn() { printf '[.ai] WARN: %s\n' "$*" >&2; }
ai_die()  { printf '[.ai] ERROR: %s\n' "$*" >&2; exit 1; }

# ---------------------------------------------------------------------------
# ai_git — git с ЯВНЫМ core.quotepath=off. Весь git в обёртках идёт через него.
#
# ГОЧА maERP (2026-09-13): почти все пути исходников кириллические
# (`src/cf/src/Documents/ЗаказПокупателя/...`). С умолчанием git
# (core.quotepath=true) заголовок диффа выглядит как
# `+++ "b/src/cf/src/Documents/\320\227\320\260..."` — в кавычках и восьмеричными
# байтами. Тогда `^+++ b/` не находит файл вовсе: дифф считается «0 файлов»,
# паёк собирается не по тем каталогам, а ai_changed_has не видит префиксов.
# В этом репо `off` стоит только в локальном .git/config — свежий клон, воркер
# или чужая машина получат кавычки. Поэтому не полагаемся на конфиг.
# ---------------------------------------------------------------------------
ai_git() { git -c core.quotepath=off "$@"; }

# ---------------------------------------------------------------------------
# Task slugs / directories. A "task" groups one workflow's artifacts under
# .ai/state/<slug>/ (gitignored transcripts) and .ai/reviews/<slug>/ (committed
# findings). Slug = lowercased, non-alnum -> '-', collapsed, timestamped if bare.
# ---------------------------------------------------------------------------
ai_slugify() {
  local raw="$1"
  local slug
  slug=$(printf '%s' "$raw" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')
  [ -n "$slug" ] || slug="task"
  printf '%.60s' "$slug"
}

ai_task_dirs() {
  # Usage: ai_task_dirs <slug> -> sets AI_TASK_STATE_DIR / AI_TASK_REVIEW_DIR
  local slug="$1"
  AI_TASK_STATE_DIR="$AI_STATE/$slug"
  AI_TASK_REVIEW_DIR="$AI_REVIEWS/$slug"
  mkdir -p "$AI_TASK_STATE_DIR" "$AI_TASK_REVIEW_DIR"
}

ai_timestamp() { date -u +%Y%m%dT%H%M%SZ; }

# ---------------------------------------------------------------------------
# Portable timeout. macOS has no `timeout`(1) by default (confirmed missing
# 2026-09-11) and we don't want a hard dependency on coreutils' gtimeout.
#
# ai_with_timeout <secs> <stdin_file|-> <cmd...>  — runs cmd, kills it (and
# its descendants) after <secs>, returns cmd's exit code (124 if killed).
#
# GOTCHA (verified 2026-09-11): an asynchronous command (`cmd &`) in a
# non-interactive shell gets /dev/null as stdin UNLESS the backgrounded
# command itself carries an explicit redirect — a redirect on an ANCESTOR
# shell/function is not enough, bash only honors one attached to the async
# command's own syntax. That's why <stdin_file> is a required, explicit
# argument here instead of relying on the caller's `< file` before calling
# this function — that pattern silently fed codex an empty stdin.
# Pass "-" for stdin_file when the command doesn't read stdin.
#
# GOTCHA (Codex adversarial review, 2026-09-11): the backgrounded `( "$@";
# echo $? > file ) &` is a REAL wrapper shell process (confirmed via `ps` —
# it does not exec-optimize away, because there's a second command after
# "$@"), so `$!` is that wrapper's PID, not the actual codex/opencode
# process — that's a CHILD of it. Killing only `$!` on timeout left the real
# backend (and anything it forked) running past the deadline, still
# consuming API quota / writing state after the wrapper had already reported
# failure. `set -m` + negative-PID process-group kill was the first idea but
# non-interactive scripts don't reliably get one without side effects on
# signal handling; `pgrep -P` walking the actual process tree (verified with
# `ps`/`pgrep -P` against this exact two-command subshell shape) is more
# portable and doesn't touch job control at all.
# ---------------------------------------------------------------------------
ai_pid_tree() {
  # Prints <root> plus every descendant PID, BFS via pgrep -P (no job
  # control / process-group assumptions needed).
  local root="$1"
  local frontier="$root" all="$root" kids
  while [ -n "$frontier" ]; do
    kids=""
    for p in $frontier; do
      kids="$kids $(pgrep -P "$p" 2>/dev/null)"
    done
    kids="$(printf '%s\n' "$kids" | tr ' ' '\n' | grep -v '^$' | sort -u)"
    [ -z "$kids" ] && break
    all="$all
$kids"
    frontier="$kids"
  done
  printf '%s\n' "$all" | sort -u
}

ai_kill_tree() {
  local root="$1" sig="${2:-TERM}"
  local pid
  ai_pid_tree "$root" | while IFS= read -r pid; do
    [ -n "$pid" ] && kill "-$sig" "$pid" 2>/dev/null
  done
}

ai_with_timeout() {
  local secs="$1" stdin_file="$2"; shift 2
  local out_rc_file
  out_rc_file=$(mktemp)
  if [ "$stdin_file" = "-" ]; then
    (
      "$@"
      echo $? > "$out_rc_file"
    ) &
  else
    (
      "$@" < "$stdin_file"
      echo $? > "$out_rc_file"
    ) &
  fi
  local cmd_pid=$!
  (
    sleep "$secs"
    if kill -0 "$cmd_pid" 2>/dev/null; then
      ai_kill_tree "$cmd_pid" TERM
      sleep 2
      ai_kill_tree "$cmd_pid" KILL
    fi
  ) &
  local watcher_pid=$!
  wait "$cmd_pid" 2>/dev/null
  local rc=124
  [ -s "$out_rc_file" ] && rc=$(cat "$out_rc_file")
  kill "$watcher_pid" 2>/dev/null
  wait "$watcher_pid" 2>/dev/null
  rm -f "$out_rc_file"
  return "$rc"
}

# ---------------------------------------------------------------------------
# Backend availability. Never simulate a result when a backend is missing —
# every ai-* wrapper must check these and exit with BACKEND_UNAVAILABLE
# instead of guessing. See FAILURE HANDLING in .ai/README.md.
# ---------------------------------------------------------------------------
ai_codex_available() {
  [ "$AI_CODEX_ENABLED" = "1" ] || return 1
  command -v "$AI_CODEX_BIN" >/dev/null 2>&1 || return 1
  # `codex login status` exits 0 and prints "Logged in..." when authorized.
  "$AI_CODEX_BIN" login status >/dev/null 2>&1
}

ai_opencode_available() {
  [ "$AI_OPENCODE_ENABLED" = "1" ] || return 1
  command -v "$AI_OPENCODE_BIN" >/dev/null 2>&1
  # No credential check here: the opencode/* zen tier (default model) works
  # with zero configured providers (verified 2026-09-11, cost:0). A real
  # failure (rate limit, model gone, missing OPENCODE_API_KEY for an
  # opencode-go/* model, Go subscription limit exhausted) surfaces from
  # ai_run_opencode's own exit-code / error-event check, not from a static
  # credentials probe.
}

# ai_with_timeout_first_output <secs> <first_output_secs> <watch_file> <stdin_file|-> <cmd...>
# Как ai_with_timeout, но дополнительно снимает процесс, если <watch_file> остаётся пустым
# дольше <first_output_secs> — тогда код возврата 125.
#
# Зачем (проверено 2026-09-13): исчерпанный лимит подписки OpenCode Go не даёт ни ошибки,
# ни события — `opencode run` молча висит без единого байта в stdout и stderr до общего
# таймаута. Ревью ждало 600 с вместо того, чтобы сразу перейти на запасную модель.
# 0 в <first_output_secs> отключает сторож.
ai_with_timeout_first_output() {
  local secs="$1" first_secs="$2" watch_file="$3" stdin_file="$4"; shift 4
  local out_rc_file stall_file
  out_rc_file=$(mktemp)
  stall_file=$(mktemp)
  rm -f "$stall_file"
  if [ "$stdin_file" = "-" ]; then
    (
      "$@"
      echo $? > "$out_rc_file"
    ) &
  else
    (
      "$@" < "$stdin_file"
      echo $? > "$out_rc_file"
    ) &
  fi
  local cmd_pid=$!
  (
    local waited=0
    while kill -0 "$cmd_pid" 2>/dev/null; do
      if [ "$waited" -ge "$secs" ]; then
        break
      fi
      if [ "$first_secs" -gt 0 ] && [ "$waited" -ge "$first_secs" ] && [ ! -s "$watch_file" ]; then
        : > "$stall_file"
        break
      fi
      sleep 2
      waited=$((waited + 2))
    done
    if kill -0 "$cmd_pid" 2>/dev/null; then
      ai_kill_tree "$cmd_pid" TERM
      sleep 2
      ai_kill_tree "$cmd_pid" KILL
    fi
  ) &
  local watcher_pid=$!
  wait "$cmd_pid" 2>/dev/null
  local rc=124
  [ -s "$out_rc_file" ] && rc=$(cat "$out_rc_file")
  [ -e "$stall_file" ] && rc=125
  kill "$watcher_pid" 2>/dev/null
  wait "$watcher_pid" 2>/dev/null
  rm -f "$out_rc_file" "$stall_file"
  return "$rc"
}

# ---------------------------------------------------------------------------
# Codex runner. ALWAYS read-only unless a caller explicitly overrides
# AI_CODEX_SANDBOX — reviewers must never be able to write to the repo.
#
# ai_run_codex <prompt_file> <result_json_out> <events_log_out> [extra codex args...]
# Returns codex's exit code. On success, <result_json_out> holds the final
# structured message (requires the caller to have passed --output-schema via
# extra args, or accept free-text).
# ---------------------------------------------------------------------------
ai_run_codex() {
  local prompt_file="$1" result_out="$2" events_out="$3"; shift 3
  local model_args=()
  [ -n "$AI_CODEX_MODEL" ] && model_args=(-m "$AI_CODEX_MODEL")

  ai_log "codex exec (-s $AI_CODEX_SANDBOX) -> $result_out"
  ai_with_timeout "$AI_CODEX_TIMEOUT_SECS" "$prompt_file" \
    "$AI_CODEX_BIN" exec --skip-git-repo-check -C "$AI_REPO_ROOT" \
      -s "$AI_CODEX_SANDBOX" \
      "${model_args[@]+"${model_args[@]}"}" \
      --json \
      -o "$result_out" \
      "$@" \
      - > "$events_out" 2>"${events_out}.stderr"
  local rc=$?
  if [ "$rc" -eq 124 ]; then
    ai_warn "codex exec timed out after ${AI_CODEX_TIMEOUT_SECS}s"
  elif [ "$rc" -ne 0 ]; then
    ai_warn "codex exec exited $rc — see ${events_out}.stderr"
  fi
  return "$rc"
}

# ---------------------------------------------------------------------------
# OpenCode runner.
# ai_run_opencode <agent_name> <message_or_-for-file> <events_json_out> [file_to_attach]
# Writes the raw JSONL event stream to <events_json_out> and echoes the
# concatenated assistant text to stdout. Returns non-zero on any error event
# or non-zero exit — never returns success with fabricated content.
# ---------------------------------------------------------------------------
ai_run_opencode() {
  local agent="$1" message="$2" events_out="$3"
  shift 3
  # Основная модель, затем запасные (AI_OPENCODE_FALLBACK_MODELS): лимит подписки Go
  # не должен останавливать ревью, пока жива бесплатная модель Zen. Транскрипт каждой
  # попытки — свой файл; итоговый <events_json_out> — транскрипт успешной модели.
  local models="$AI_OPENCODE_MODEL $AI_OPENCODE_FALLBACK_MODELS"
  local model attempt_events rc=1 tried=""
  for model in $models; do
    case " $tried " in *" $model "*) continue ;; esac
    tried="$tried $model"
    if [ "$model" = "$AI_OPENCODE_MODEL" ]; then
      attempt_events="$events_out"
    else
      attempt_events="${events_out%.jsonl}-$(printf '%s' "$model" | tr '/:' '__').jsonl"
      ai_warn "opencode: switching to fallback model $model"
    fi
    local text
    text=$(ai_run_opencode_model "$agent" "$model" "$message" "$attempt_events" "$@")
    rc=$?
    if [ "$rc" -eq 0 ]; then
      [ "$attempt_events" != "$events_out" ] && cp "$attempt_events" "$events_out"
      # Модель — первой строкой отчёта: ревью запасной бесплатной моделью слабее, и это
      # должно быть видно в самом артефакте, а не только в логе обёртки.
      if [ "$model" = "$AI_OPENCODE_MODEL" ]; then
        printf '_OpenCode: модель %s._\n\n' "$model"
      else
        printf '_OpenCode: запасная модель %s — основная %s не ответила (лимит, зависание или ошибка)._\n\n' \
          "$model" "$AI_OPENCODE_MODEL"
      fi
      printf '%s\n' "$text"
      return 0
    fi
  done
  return "$rc"
}

# ai_run_opencode_model <agent_name> <model> <message> <events_json_out> [file_to_attach]
# Один прогон OpenCode на одной модели; контракт возврата — как у ai_run_opencode.
ai_run_opencode_model() {
  local agent="$1" model="$2" message="$3" events_out="$4"
  shift 4
  local file_args=()
  for f in "$@"; do file_args+=(-f "$f"); done

  ai_log "opencode run --agent $agent -m $model -> $events_out"
  ai_with_timeout_first_output "$AI_OPENCODE_TIMEOUT_SECS" "$AI_OPENCODE_FIRST_EVENT_SECS" "$events_out" - \
    "$AI_OPENCODE_BIN" run --format json --agent "$agent" -m "$model" \
      "${file_args[@]+"${file_args[@]}"}" "$message" \
      --dir "$AI_REPO_ROOT" \
      > "$events_out" 2>"${events_out}.stderr"
  local rc=$?
  if [ "$rc" -eq 125 ]; then
    ai_warn "opencode run ($model): no output in ${AI_OPENCODE_FIRST_EVENT_SECS}s — stalled (likely subscription limit)"
    return "$rc"
  fi
  if [ "$rc" -eq 124 ]; then
    ai_warn "opencode run ($model) timed out after ${AI_OPENCODE_TIMEOUT_SECS}s"
    return "$rc"
  fi
  if [ "$rc" -ne 0 ]; then
    ai_warn "opencode run exited $rc — see ${events_out}.stderr"
    return "$rc"
  fi
  if grep -q '"type":"error"' "$events_out" 2>/dev/null; then
    ai_warn "opencode run reported an error event — see $events_out"
    return 1
  fi
  # Concatenate all text parts in order (jq if available, grep/sed fallback).
  local extracted
  if command -v jq >/dev/null 2>&1; then
    extracted=$(jq -rs '[.[] | select(.type=="text") | .part.text] | join("\n")' "$events_out" 2>/dev/null)
  else
    extracted=$(grep -o '"type":"text"[^}]*"text":"[^"]*"' "$events_out" | sed -E 's/.*"text":"([^"]*)".*/\1/')
  fi
  # An opencode exit-0 with no error event but no (or whitespace-only)
  # extractable text is still not a success — Codex's review caught that the
  # old version returned 0 here unconditionally, so a jq-parse failure or an
  # empty response silently became an "empty but successful" report, and the
  # dual-backend caller (ai_run_specialist_review) never fell through to the
  # Codex fallback because opencode had technically "succeeded."
  if [ -z "$(printf '%s' "$extracted" | tr -d '[:space:]')" ]; then
    ai_warn "opencode run produced no usable text (exit 0, no error event, but empty/unparseable output) — see $events_out"
    return 1
  fi
  printf '%s\n' "$extracted"
  return 0
}

# ---------------------------------------------------------------------------
# Diff collection for review wrappers.
# ai_collect_diff <mode> where mode is one of:
#   working              -- staged + unstaged changes vs HEAD (default)
#   base:<branch>        -- changes vs merge-base with <branch> (PR-style diff)
#   commit:<sha>          -- a single commit
# Prints the unified diff to stdout, plus an "untracked files" listing (git
# diff doesn't cover those) appended as a comment block.
#
# Returns non-zero if the git commands themselves fail (bad branch name, bad
# sha, etc) — Codex's review caught that the old version silently swallowed
# these: `--base <typo'd-branch>` made `git merge-base` fail, the empty
# result turned into `git diff ..HEAD` (also an error), and the caller's
# "empty output = nothing changed, exit 0" logic reported success for a
# MANDATORY review that never actually ran. Callers MUST check this
# function's exit status before treating empty output as "nothing changed."
#
# ДОКИ ИСКЛЮЧЕНЫ ПО УМОЛЧАНИЮ (`docs/**`, `.ai/**`). Замер 2026-09-11: запись в
# журнал + строки в RULES/ROUTING раздули промпт ревью с 20 до 33 КБ — платим
# за прозу, которую ревьюер кода всё равно не проверяет. Док-дифф нужен в
# ревью редко и осознанно: `AI_DIFF_WITH_DOCS=1` или флаг `--with-docs`.
# CLAUDE.md и AGENTS.md НЕ исключаем — это правила, их правки ревьюить надо.
# ---------------------------------------------------------------------------
ai_collect_diff() {
  local mode="${1:-working}"
  cd "$AI_REPO_ROOT" || return 1
  local -a pathspec=()
  if [ "${AI_DIFF_WITH_DOCS:-0}" != "1" ]; then
    pathspec=(-- . ':(exclude)docs/**' ':(exclude).ai/**')
  fi
  # Тело собираем в переменную, а не печатаем на ходу: вызывающий отличает
  # «ревьюить нечего» от «git упал» по ПУСТОМУ выводу, и служебная приписка про
  # исключённые доки не должна превращать пустой дифф в непустой.
  local body=""
  case "$mode" in
    working)
      body=$(ai_git diff HEAD "${pathspec[@]+"${pathspec[@]}"}") || return 1
      ;;
    base:*)
      local branch="${mode#base:}" base_sha
      base_sha="$(ai_git merge-base "$branch" HEAD 2>&1)" || {
        ai_warn "git merge-base $branch HEAD failed: $base_sha"
        return 1
      }
      body=$(ai_git diff "$base_sha"..HEAD "${pathspec[@]+"${pathspec[@]}"}") || return 1
      ;;
    commit:*)
      local sha="${mode#commit:}"
      body=$(ai_git show "$sha" "${pathspec[@]+"${pathspec[@]}"}") || return 1
      ;;
    *)
      ai_warn "unknown diff mode: $mode — defaulting to working"
      body=$(ai_git diff HEAD "${pathspec[@]+"${pathspec[@]}"}") || return 1
      ;;
  esac
  local untracked
  untracked=$(ai_git status --porcelain | grep '^??' | sed 's/^?? /  /')
  if [ "${AI_DIFF_WITH_DOCS:-0}" != "1" ] && [ -n "$untracked" ]; then
    untracked=$(printf '%s\n' "$untracked" | grep -vE '^\s+(docs/|\.ai/)' || true)
  fi
  [ -n "$body" ] && printf '%s\n' "$body"
  if [ -n "$untracked" ]; then
    printf '\n# --- untracked files (not in the diff above, read them directly if relevant) ---\n%s\n' "$untracked"
  fi
  if [ -n "$body$untracked" ] && [ "${AI_DIFF_WITH_DOCS:-0}" != "1" ]; then
    printf '\n# --- docs/** и .ai/** исключены из этого диффа (правки доков и самой оркестрации ревью кода не касаются; нужны — перезапусти с --with-docs) ---\n'
  fi
  return 0
}

# ---------------------------------------------------------------------------
# Снимок рабочего дерева как git-tree — база для инкрементального ревью
# (`ai-review --verify`: «что изменилось С ПРОШЛОГО ревью»).
#
# Пишем во ВРЕМЕННЫЙ индекс (GIT_INDEX_FILE), поэтому настоящий индекс
# пользователя не трогается вовсе — ни staged-состояние, ни `git status`.
# `git add -A` уважает .gitignore, так что untracked-новьё в снимок попадает,
# а node_modules и .ai/state — нет. Объекты остаются висячими (на них нет
# ссылок) и уедут при ближайшем `git gc` — это нормально, снимок живёт один
# цикл ревью.
# ---------------------------------------------------------------------------
ai_snapshot_tree() {
  cd "$AI_REPO_ROOT" || return 1
  local idx tree
  idx=$(mktemp -u "${TMPDIR:-/tmp}/ai-review-index.XXXXXX")
  GIT_INDEX_FILE="$idx" ai_git read-tree HEAD 2>/dev/null || { rm -f "$idx"; return 1; }
  GIT_INDEX_FILE="$idx" ai_git add -A . >/dev/null 2>&1 || { rm -f "$idx"; return 1; }
  tree=$(GIT_INDEX_FILE="$idx" ai_git write-tree 2>/dev/null) || { rm -f "$idx"; return 1; }
  rm -f "$idx"
  [ -n "$tree" ] || return 1
  printf '%s\n' "$tree"
}

# ai_tree_delta <old-tree> <new-tree> — дифф между двумя снимками, с теми же
# исключениями (docs/**, .ai/**), что и у обычного ревью.
ai_tree_delta() {
  local old="$1" new="$2"
  cd "$AI_REPO_ROOT" || return 1
  local -a pathspec=()
  if [ "${AI_DIFF_WITH_DOCS:-0}" != "1" ]; then
    pathspec=(-- . ':(exclude)docs/**' ':(exclude).ai/**')
  fi
  ai_git diff-tree -p --no-commit-id -M "$old" "$new" "${pathspec[@]+"${pathspec[@]}"}" || return 1
}

# ---------------------------------------------------------------------------
# ai_diff_tier <diff> — насколько дорогое ревью заслуживает этот дифф:
# `trivial` | `normal` | `risky`.
#
# Правило «тривиальную правку Codex не ревьюит» без механики не работает —
# платного ревьюера звали бы на любую мелочь. Здесь механика.
#
# ВАЖНО: маркеры риска ПЕРЕВЕШИВАЮТ размер. Однострочник, который трогает
# структуру хранения данных, проведение, транзакции, права, деньги, обработчики
# обновления или сборку поставки, — не тривиальный: ровно в таких строчках у
# maERP и случались инциденты (DateTime в .mdo валил загрузку конфигурации,
# подменённый запрос динсписка, реструктуризация регистров у клиента).
# Сомневаешься — это `normal`, а не `trivial`.
#
# Маркеры двух видов, и считаются они по-разному:
#   AI_RISK_PATH_RE — по заголовкам диффа (`+++ b/<путь>`, удаление, переименование):
#     сам факт правки такого файла уже риск;
#   AI_RISK_LINE_RE — только по ИЗМЕНЁННЫМ строкам (`+`/`-`), не по контексту:
#     иначе `Движения.` в трёх строках контекста вокруг правки опечатки в
#     комментарии делали бы любую правку модуля документа «рискованной».
# Кириллица в шаблонах пишется в каноническом регистре 1С: на -i для неё не
# полагаемся (проверено: совпадения одинаковы в C, C.UTF-8, ru_RU.UTF-8).
# `Запрос.Выполнить()` — не маркер: отсекается точкой перед именем, маркер
# только голые `Выполнить(`/`Вычислить(` — исполнение произвольного кода.
# Маркеры — основы слов, а не полные идентификаторы: смоук 2026-09-13 показал,
# что удалённая строка `Блокировка.Заблокировать();` (гонка за остатки) при
# маркере `БлокировкаДанных` классифицировалась как trivial и ревью не звалось.
#
# Все подсчёты через `grep -c` (читает ввод до конца), НЕ `grep -q`: см. гочу
# у ai_changed_has про SIGPIPE под pipefail.
# ---------------------------------------------------------------------------
AI_TRIVIAL_MAX_LINES="${AI_TRIVIAL_MAX_LINES:-30}"
AI_TRIVIAL_MAX_FILES="${AI_TRIVIAL_MAX_FILES:-3}"
# Хранение данных и реструктуризация; права и сеансы; очереди; поставка и деплой.
AI_RISK_PATH_RE='^\+\+\+ b/src/cf/src/(AccumulationRegisters|InformationRegisters|AccountingRegisters|CalculationRegisters|ChartsOfAccounts|ChartsOfCharacteristicTypes|ChartsOfCalculationTypes|Sequences|Constants|ExchangePlans)/[^/]+/[^/]+\.mdo'
AI_RISK_PATH_RE+='|^\+\+\+ b/src/cf/src/(Roles|SessionParameters|ScheduledJobs|EventSubscriptions|HTTPServices|WebServices)/'
AI_RISK_PATH_RE+='|^\+\+\+ b/scripts/(env|dist-build|push-release-to-hub|release-notes|changelog|ib-create|ib-restore|cf-load|cf-dump|xml-load|xml-dump|initial-fill[^/]*)\.sh'
AI_RISK_PATH_RE+='|^\+\+\+ b/\.github/|^\+\+\+ b/\.mcp\.json|^deleted file mode|^rename from'
# Типы и свойства метаданных, запрос динсписка, транзакции и блокировки,
# проведение, деньги, привилегии и пользователи, секреты, внешний код и файлы,
# обработчики обновления и первый запуск, фоновые задания.
AI_RISK_LINE_RE='<types>|<privileged>|<compatibilityMode>|<dataLockControlMode>|<queryText>|<customQuery>|<mainTable>'
AI_RISK_LINE_RE+='|НачатьТранзакцию|ЗафиксироватьТранзакцию|ОтменитьТранзакцию|Блокировк|Заблокировать|ОбменДанными\.Загрузка'
AI_RISK_LINE_RE+='|ОбработкаПроведения|ОбработкаУдаленияПроведения|Движения|НаборЗаписей|Отказ ='
AI_RISK_LINE_RE+='|Себестоимост|НДС|Взаиморасч|ДенежныеСредства|Оплат|КурсыВалют'
AI_RISK_LINE_RE+='|ПривилегированныйРежим|РольДоступна|ПравоДоступа|ПользователиИнформационнойБазы|ПараметрыСеанса|БезопасныйРежим'
AI_RISK_LINE_RE+='|Пароль|password|passwd|secret|token|hmac|api[_-]?key|SMOKE_PWD'
AI_RISK_LINE_RE+='|HTTPСоединение|HTTPЗапрос|COMОбъект|КомандаСистемы|ЗапуститьПриложение|ВнешниеОбработки|ВнешниеОтчеты|[[:space:]=(]Выполнить\(|[[:space:]=(]Вычислить\(|УдалитьФайлы'
AI_RISK_LINE_RE+='|ОбновлениеДанных|ОбработчикиОбновления|ВерсииПодсистем|НачальноеЗаполнение|ФоновыеЗадания|РегламентныеЗадания'
ai_diff_tier() {
  local diff="$1"
  local files lines risky_path risky_line
  files=$(printf '%s\n' "$diff" | grep -c '^+++ b/' || true)
  lines=$(printf '%s\n' "$diff" | grep -cE '^[+-][^+-]' || true)
  risky_path=$(printf '%s\n' "$diff" | grep -cE "$AI_RISK_PATH_RE" || true)
  risky_line=$(printf '%s\n' "$diff" | grep -E '^[+-][^+-]' | grep -ciE "$AI_RISK_LINE_RE" || true)
  if [ "${risky_path:-0}" -gt 0 ] || [ "${risky_line:-0}" -gt 0 ]; then
    printf 'risky\n'
  elif [ "${files:-0}" -le "$AI_TRIVIAL_MAX_FILES" ] && [ "${lines:-0}" -le "$AI_TRIVIAL_MAX_LINES" ]; then
    printf 'trivial\n'
  else
    printf 'normal\n'
  fi
}

# ---------------------------------------------------------------------------
# Dual-backend specialist review (used by ai-database / ai-security).
# Tries OpenCode's specialist agent first (free zen tier); on any failure or
# unavailability, falls back to Codex read-only with the same prompt. Only
# returns BACKEND_UNAVAILABLE (rc=2) if BOTH are unavailable.
#
# ai_run_specialist_review <role> <opencode_agent> <prompt_file> <result_json> <events_prefix>
# role is just used for log messages. Writes JSON (schema-shaped from Codex,
# or free text from OpenCode saved as {"summary":...,"verdict":"unknown",...}
# is NOT attempted — OpenCode's zen tier has no --output-schema equivalent,
# so its output is saved as markdown, not forced into the JSON contract).
# ---------------------------------------------------------------------------
ai_run_specialist_review() {
  local role="$1" opencode_agent="$2" prompt_file="$3" result_out="$4" events_prefix="$5"
  local order="${6:-opencode-first}"

  # codex-first — обязательные ревью (данные, безопасность). Замер 2026-09-13
  # (.ai/reports/model-bench-2026-09-13.md): на сложном диффе модели OpenCode нашли 0 из 8
  # подтверждённых находок, gpt-6-astra — 1, субагент Claude — 8. Поэтому отчёт одного
  # OpenCode для обязательного гейта недостаточен: rc 3 = отчёт есть, гейт НЕ пройден.
  if [ "$order" = "codex-first" ]; then
    if ai_codex_available; then
      ai_log "$role: trying codex (read-only)"
      local cx_first="${events_prefix}-codex.jsonl"
      if ai_run_codex "$prompt_file" "$result_out" "$cx_first" --output-schema "$AI_SCHEMAS/findings.schema.json"; then
        ai_log "$role: codex report -> $result_out"
        echo "$result_out"
        return 0
      fi
      ai_warn "$role: codex failed (limit or error) — OpenCode даст только предварительный отчёт"
    fi
    if ai_opencode_available; then
      local oc_first="${events_prefix}-opencode.jsonl"
      local oc_first_md="${result_out%.json}.md"
      if ai_run_opencode "$opencode_agent" "$(cat "$prompt_file")" "$oc_first" > "$oc_first_md.tmp"; then
        mv "$oc_first_md.tmp" "$oc_first_md"
        ai_warn "$role: GATE_NOT_PASSED — отчёт только OpenCode ($oc_first_md); обязательный гейт — субагент Claude"
        echo "$oc_first_md"
        return 3
      fi
      rm -f "$oc_first_md.tmp"
    fi
    echo "BACKEND_UNAVAILABLE" >&2
    return 2
  fi

  if ai_opencode_available; then
    ai_log "$role: trying opencode/$opencode_agent"
    local oc_events="${events_prefix}-opencode.jsonl"
    local oc_md="${result_out%.json}.md"
    if ai_run_opencode "$opencode_agent" "$(cat "$prompt_file")" "$oc_events" > "$oc_md.tmp"; then
      mv "$oc_md.tmp" "$oc_md"
      ai_log "$role: opencode report -> $oc_md"
      echo "$oc_md"
      return 0
    fi
    rm -f "$oc_md.tmp"
    ai_warn "$role: opencode failed, falling back to codex"
  fi

  if ai_codex_available; then
    ai_log "$role: trying codex (read-only)"
    local cx_events="${events_prefix}-codex.jsonl"
    if ai_run_codex "$prompt_file" "$result_out" "$cx_events" --output-schema "$AI_SCHEMAS/findings.schema.json"; then
      ai_log "$role: codex report -> $result_out"
      echo "$result_out"
      return 0
    fi
    ai_warn "$role: codex also failed"
    return 1
  fi

  echo "BACKEND_UNAVAILABLE" >&2
  return 2
}

# List of changed files (tracked, staged+unstaged, vs HEAD) plus untracked
# ones — used by ai-test/ai-final-check to scope which real commands to run.
ai_changed_files() {
  cd "$AI_REPO_ROOT" || return 1
  # Untracked — файлами, а не каталогами (`git status` схлопывает новый каталог в
  # одну строку, а линт-гейт сверяет замечания по конкретным файлам) и без awk
  # '{print $2}', который режет путь на первом пробеле.
  { ai_git diff --name-only HEAD; ai_git ls-files --others --exclude-standard; } | sort -u
}

# ---------------------------------------------------------------------------
# ai_changed_has <file-list> <path-prefix> — есть ли в списке путь с таким
# префиксом. БЕЗ пайпа, намеренно.
#
# ГОЧА (2026-09-12, стоила молча пропущенных гейтов): привычное
# `printf '%s\n' "$LIST" | grep -q '^web/'` под `set -o pipefail` — ГОНКА.
# `grep -q` выходит на первом же совпадении, `printf` получает SIGPIPE (141),
# pipefail отдаёт 141 как код всего конвейера, и `if` уходит в else. В
# ai-final-check это выглядело как «(no web/** changes — frontend gates
# skipped)» при восьми изменённых файлах в web/ — воспроизвелось в 3 прогонах
# из 4 на одном и том же дереве. Родня инцидента с migrator'ом (`trap '' PIPE`).
# ---------------------------------------------------------------------------
ai_changed_has() {
  local list="$1" prefix="$2"
  case $'\n'"$list"$'\n' in
    *$'\n'"$prefix"*) return 0 ;;
    *) return 1 ;;
  esac
}

# ---------------------------------------------------------------------------
# ai_context_pack <changed-files> — контекстный «паёк» для внешнего ревьюера.
#
# ЗАЧЕМ (замеры эталона TinyCIO, 2026-09-11): круг ревью стоил ~350k входных
# токенов при ответе в 2.6k. Промпт в этом — 8k; остальное ревьюер набирал сам:
# `cat` правил и файлов целиком, и весь этот контекст переотправлялся на КАЖДОМ
# из 11–15 ходов. Дешевле отдать нужные куски сразу. В maERP паёк такой:
#   - срезы CLAUDE.md по заголовкам: «Где исходники» … «Проверка себя» (что
#     правится, код, именование, проверки) и «Версия и список изменений»;
#   - AGENTS.md затронутых каталогов (сейчас их в репо нет — механика на будущее);
#   - оглавление правил tiny1C (core + greenfield, по строке на правило; само
#     правило — точечным чтением его файла). MCP ревьюеру недоступен, а правила
#     tiny1C — это ровно уроки из ошибок maERP;
#   - раздел «Правила» docs/FORMS-STYLE.md — только если дифф трогает Form.form.
# ---------------------------------------------------------------------------
AI_TINY1C_HOME="${TINY1C_HOME:-$AI_REPO_ROOT/../tiny1C}"

# ai_md_slice <file> <start-heading-re> <stop-heading-re> — строки от заголовка
# до следующего нужного заголовка, сам стоп-заголовок отрезается.
ai_md_slice() {
  sed -n "/$2/,/$3/p" "$1" 2>/dev/null | sed '$d'
}

ai_context_pack() {
  local changed="${1:-}"
  cd "$AI_REPO_ROOT" || return 1
  echo "## Context pack — прочитано за тебя, эти файлы заново читать НЕ НАДО"
  echo
  # Срезы по ЗАГОЛОВКАМ CLAUDE.md. Переименуют заголовок — срез станет пустым;
  # молча отдать ревьюеру пустой паёк хуже, чем не собирать его вовсе, поэтому
  # пустота — не «ну и ладно», а явная строка с инструкцией прочитать файл.
  local rules version
  rules=$(ai_md_slice CLAUDE.md '^## Где исходники' '^## Версия и список изменений')
  version=$(ai_md_slice CLAUDE.md '^## Версия и список изменений' '^## Git')
  if [ -n "$rules" ] && [ -n "$version" ]; then
    echo "### CLAUDE.md → «Где исходники»…«Проверка себя» + «Версия и список изменений» (остальное — релизы и git, ревью кода не касается)"
    echo '```markdown'
    printf '%s\n\n%s\n' "$rules" "$version"
    echo '```'
  else
    ai_warn "ai_context_pack: срез CLAUDE.md пуст — переименовали заголовки «Где исходники»/«Версия и список изменений»/«Git»?"
    echo "### CLAUDE.md — АВТО-СРЕЗ НЕ СОБРАЛСЯ (заголовки переименованы)"
    echo "Прочитай правила сам, точечно: \`grep -n '^## ' CLAUDE.md\`, затем \`sed -n 'A,Bp' CLAUDE.md\`"
    echo "по разделам про исходники, код, именование, проверки и версию."
  fi
  echo
  # AGENTS.md затронутых каталогов: локальные правила сильнее общих.
  local -a agents=()
  local f d
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    d=$(dirname "$f")
    while [ "$d" != "." ] && [ "$d" != "/" ]; do
      [ -f "$d/AGENTS.md" ] && agents+=("$d/AGENTS.md")
      d=$(dirname "$d")
    done
  done <<< "$changed"
  if [ ${#agents[@]} -gt 0 ]; then
    local a
    while IFS= read -r a; do
      echo "### $a (локальные правила каталога)"
      echo '```markdown'
      cat "$a"
      echo '```'
      echo
    done < <(printf '%s\n' "${agents[@]}" | sort -u)
  fi
  # Оглавление tiny1C. Первая строка «# …» каждого файла — формулировка правила.
  local rules_dir idx=""
  for rules_dir in "$AI_TINY1C_HOME/tracks/core/rules" "$AI_TINY1C_HOME/tracks/greenfield/rules"; do
    [ -d "$rules_dir" ] || continue
    for f in "$rules_dir"/*.md; do
      [ -f "$f" ] || continue
      idx+="$(basename "$f" .md): $(sed -n '/^# /{s/^# //p;q;}' "$f")"$'\n'
    done
  done
  if [ -n "$idx" ]; then
    echo "### Правила tiny1C (уроки из ошибок maERP) — только оглавление"
    echo '```text'
    printf '%s' "$idx"
    echo '```'
    echo "Правило целиком (файлы по 1–4 КБ) — точечно: \`sed -n '1,80p' $AI_TINY1C_HOME/tracks/core/rules/<id>.md\`"
    echo "(у gf-* каталог \`tracks/greenfield/rules\`). Нарушение правила из этого списка — не вкусовщина, а находка."
  else
    ai_warn "ai_context_pack: правила tiny1C не найдены в $AI_TINY1C_HOME (TINY1C_HOME) — паёк без них"
    echo "### Правила tiny1C — НЕ НАЙДЕНЫ ($AI_TINY1C_HOME)"
    echo "Сверяйся с \`docs/rules-1c/\` точечно (\`rg -n '<тема>' docs/rules-1c --glob '!unica/**'\`), не читая файлы целиком."
  fi
  echo
  local forms
  forms=$(printf '%s\n' "$changed" | grep -c '/Form\.form$' || true)
  if [ "${forms:-0}" -gt 0 ]; then
    local style
    style=$(ai_md_slice docs/FORMS-STYLE.md '^## Правила' '^## Как править')
    if [ -n "$style" ]; then
      echo "### docs/FORMS-STYLE.md → «Правила» (дифф трогает Form.form)"
      echo '```markdown'
      printf '%s\n' "$style"
      echo '```'
    else
      ai_warn "ai_context_pack: срез «Правила» из docs/FORMS-STYLE.md пуст — переименовали заголовок?"
      echo "### docs/FORMS-STYLE.md — АВТО-СРЕЗ НЕ СОБРАЛСЯ: \`grep -n '^## ' docs/FORMS-STYLE.md\` и читай раздел правил точечно."
    fi
    echo
  fi
}

# Pretty-print a findings.schema.json-shaped result for a human (used by
# several wrappers after ai_run_codex succeeds).
ai_print_findings_summary() {
  local json_file="$1"
  [ -f "$json_file" ] || { ai_warn "no result file: $json_file"; return 1; }
  if ! command -v jq >/dev/null 2>&1; then
    cat "$json_file"
    return 0
  fi
  jq -r '
    "Verdict: \(.verdict)\nSummary: \(.summary)\n",
    (.findings | length | "Findings: \(.)"),
    (.findings[] | "  [\(.severity)] \(.file):\(.location) — \(.problem)")
  ' "$json_file" 2>/dev/null || cat "$json_file"
}

# ---------------------------------------------------------------------------
# ai_new_files — добавленные файлы: новые в индексе (A) плюс untracked.
# ---------------------------------------------------------------------------
ai_new_files() {
  cd "$AI_REPO_ROOT" || return 1
  { ai_git diff --name-only --diff-filter=A HEAD; ai_git ls-files --others --exclude-standard; } | sort -u
}

# ---------------------------------------------------------------------------
# ai_regimen_warnings <changed> <new> — пункт 2 регламента docs/TESTING.md:
# «новый функционал расширяет тесты». Печатает предупреждения (по строке), код
# возврата всегда 0: это напоминание, а не гейт — какой сценарий нужен, решает
# человек, а формы в смок попадают перебором автоматически.
# ---------------------------------------------------------------------------
ai_regimen_warnings() {
  local changed="$1" new="$2" n
  n=$(printf '%s\n' "$new" | grep -cE '^src/cf/src/Documents/[^/]+/[^/]+\.mdo$' || true)
  if [ "${n:-0}" -gt 0 ] && ! ai_changed_has "$changed" "src/cf/src/DataProcessors/ТестыДокументов/"; then
    echo "новый документ ($n шт.), а ТестыДокументов не менялась — сценарий создания/записи/проведения нужен (docs/TESTING.md, регламент п. 2)"
  fi
  n=$(printf '%s\n' "$new" | grep -cE '^src/cf/src/.+/(Forms/[^/]+/Form\.form|[^/]+\.mdo)$' || true)
  if [ "${n:-0}" -gt 0 ] && ! ai_changed_has "$changed" "docs/TESTS.xlsx"; then
    echo "новые объекты/формы ($n файлов), а реестр docs/TESTS.xlsx не менялся — изменение состава тестов фиксируется в реестре"
  fi
  if ai_changed_has "$changed" "src/cf/src/"; then
    echo "уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки"
  fi
  return 0
}
