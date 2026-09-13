#!/usr/bin/env bash
# .ai/config.sh — central config for the maERP AI orchestration layer.
# Sourced by every script in .ai/bin/. Override any AI_* var in your shell env
# or in .ai/config.local.sh (gitignored) — never edit this file for a one-off run.

# Repo root — resolved relative to this file, not $PWD, so wrappers work from any cwd.
AI_REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

AI_DIR="$AI_REPO_ROOT/.ai"
AI_BIN="$AI_DIR/bin"
AI_PROMPTS="$AI_DIR/prompts"
AI_SCHEMAS="$AI_DIR/schemas"
AI_REVIEWS="$AI_DIR/reviews"
AI_REPORTS="$AI_DIR/reports"
AI_STATE="$AI_DIR/state"

# --- Codex --------------------------------------------------------------
# Verified 2026-09-11: codex-cli 0.154.0, logged in via ChatGPT.
# Model/effort default to whatever ~/.codex/config.toml has (gpt-6-astra/high
# at setup time) — override only if you need to pin a specific model.
AI_CODEX_BIN="${AI_CODEX_BIN:-codex}"
AI_CODEX_MODEL="${AI_CODEX_MODEL:-}"            # empty = use codex's own config default
AI_CODEX_SANDBOX="${AI_CODEX_SANDBOX:-read-only}" # never override to workspace-write from a wrapper
AI_CODEX_TIMEOUT_SECS="${AI_CODEX_TIMEOUT_SECS:-600}"

# --- OpenCode -------------------------------------------------------------
# Verified 2026-09-11: opencode 1.18.30 (brew, tap sst/tap), zero provider
# credentials configured. The `opencode/*` zen tier works with NO login and
# NO cost (cost:0 in step_finish events) — that's what these wrappers use by
# default. `opencode/big-pickle` looked like the strongest general model of
# the free set at setup time (others are explicitly "-free"/flash/lightning
# variants). If you later run `opencode providers login` to add a paid
# provider (Anthropic/OpenAI/etc.), point AI_OPENCODE_MODEL at it — stronger
# model, same wrapper.
# OpenCode Go subscription: models are `opencode-go/*` (NOT `opencode/*` —
# those are Zen, billed from credits). Set it in .ai/config.local.sh, not
# here — see «OpenCode Go» in .ai/README.md.
AI_OPENCODE_BIN="${AI_OPENCODE_BIN:-opencode}"
AI_OPENCODE_MODEL="${AI_OPENCODE_MODEL:-opencode/big-pickle}"
# 600s not 300s: observed a real timeout at 300s reviewing a genuinely large
# diff (34 files/1881 lines) on the free-tier model — it correctly fell back
# to Codex per FAILURE HANDLING rather than fabricating anything, but a
# larger default avoids paying the fallback tax for merely-large diffs.
AI_OPENCODE_TIMEOUT_SECS="${AI_OPENCODE_TIMEOUT_SECS:-600}"

# --- Backend availability (probed lazily by ai-lib.sh, not here) --------
# AI_OPENCODE_ENABLED lets a human hard-disable the OpenCode path without
# uninstalling it (e.g. zen tier rate-limited for the day).
AI_OPENCODE_ENABLED="${AI_OPENCODE_ENABLED:-1}"
AI_CODEX_ENABLED="${AI_CODEX_ENABLED:-1}"

# Load machine/user overrides if present (gitignored).
if [ -f "$AI_DIR/config.local.sh" ]; then
  # shellcheck source=/dev/null
  source "$AI_DIR/config.local.sh"
fi
