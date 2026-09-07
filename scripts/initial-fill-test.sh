#!/usr/bin/env bash
# Тест headless-первого запуска: пустая база из CF → initial-fill.sh с образцом payload →
# повторный запуск ничего не создаёт → в базе есть организация и пользователи (условие
# визарда «ноль организаций и ноль пользователей» больше не выполняется) → smoke.sh под
# созданным администратором проходит.
# Использование: scripts/initial-fill-test.sh <файл.cf> [каталог-базы]
#   каталог-базы по умолчанию build/ib-initial - ПЕРЕСОЗДАЁТСЯ; build/ib скрипт не трогает.
#   INITIAL_FILL_NO_SMOKE=1 - без шага smoke.sh (быстрая проверка заполнения).
# CF собирается из обновлённой build/ib: scripts/dist-build.sh (docs/TESTING.md).
#
# Пароли для теста генерируются на лету и живут только в переменных окружения и во
# временном payload-файле с правами 600, который удаляется по завершении.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

CF="${1:?Укажи путь к .cf}"
IB="${2:-$BUILD/ib-initial}"
EXAMPLE="$ROOT/scripts/initial-fill.example.json"
RESULT1="$BUILD/initial-fill-test-1.json"
RESULT2="$BUILD/initial-fill-test-2.json"

case "$IB" in "$IB_BUILD"|"$IB_BUILD/") echo "Тест пересоздаёт базу - build/ib для него не подходит" >&2; exit 1;; esac

PAYLOAD="$(mktemp "$BUILD/initial-fill-test.XXXXXX")"
chmod 600 "$PAYLOAD"
trap 'rm -f "$PAYLOAD"' EXIT

random_password() { LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 20; }
ADMIN_LOGIN="fatima"
ADMIN_PWD="$(random_password)"
OTHER_PWD="$(random_password)"
SUPPORT_PWD="$(random_password)"
export ADMIN_PWD OTHER_PWD SUPPORT_PWD
python3 - "$EXAMPLE" "$PAYLOAD" <<'EOF'
import json, os, sys
src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
pwds = [os.environ["ADMIN_PWD"], os.environ["OTHER_PWD"]]
for i, user in enumerate(data["users"]):
    user["password"] = pwds[i % len(pwds)]
data["support_admin"]["password"] = os.environ["SUPPORT_PWD"]
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
EOF

check_result() { # $1 — result-файл, $2 — ожидаемое organization_created (true|false)
	python3 - "$1" "$2" <<'EOF'
import json, sys
path, expected = sys.argv[1], sys.argv[2] == "true"
data = json.load(open(path, encoding="utf-8"))
problems = []
if not data.get("success"):
    problems.append("success != true")
if data.get("organization_created") != expected:
    problems.append("organization_created=%r, ожидалось %r" % (data.get("organization_created"), expected))
if data.get("support_admin_created") != expected:
    problems.append("support_admin_created=%r, ожидалось %r" % (data.get("support_admin_created"), expected))
for user in data.get("users", []):
    if user.get("created") != expected:
        problems.append("users[%s].created=%r, ожидалось %r" % (user.get("login"), user.get("created"), expected))
if not data.get("organizations_total", 0) > 0 or not data.get("users_total", 0) > 0:
    problems.append("organizations_total=%r, users_total=%r - визард первого запуска откроется"
                    % (data.get("organizations_total"), data.get("users_total")))
for key in ("password", "Пароль"):
    if key in open(path, encoding="utf-8").read():
        problems.append("в result-файле есть слово %s" % key)
if problems:
    print("\n".join("  " + p for p in problems))
    sys.exit(1)
print("  organization_created=%s users=%d organizations_total=%s users_total=%s warnings=%d" % (
    data["organization_created"], len(data.get("users", [])), data["organizations_total"],
    data["users_total"], len(data.get("warnings", []))))
EOF
}

FAILED=0

echo "== Шаг 1. Пустая база из CF =="
"$ROOT/scripts/ib-create.sh" "$CF" "$IB"

echo "== Шаг 2. Первое заполнение =="
unset SMOKE_USER SMOKE_PWD
"$ROOT/scripts/initial-fill.sh" "$IB" "$PAYLOAD" "$RESULT1" || FAILED=1
if [ "$FAILED" -eq 0 ]; then
	check_result "$RESULT1" true || FAILED=1
fi
if [ "$FAILED" -ne 0 ]; then
	echo "ТЕСТ НЕ ПРОЙДЕН: первое заполнение"
	exit 1
fi

echo "== Шаг 3. Повторное заполнение (идемпотентность) =="
export SMOKE_USER="$ADMIN_LOGIN" SMOKE_PWD="$ADMIN_PWD"
"$ROOT/scripts/initial-fill.sh" "$IB" "$PAYLOAD" "$RESULT2" || FAILED=1
if [ "$FAILED" -eq 0 ]; then
	check_result "$RESULT2" false || FAILED=1
fi
if [ "$FAILED" -ne 0 ]; then
	echo "ТЕСТ НЕ ПРОЙДЕН: повторное заполнение"
	exit 1
fi

if [ "${INITIAL_FILL_NO_SMOKE:-0}" = "1" ]; then
	echo "Шаг 4 (smoke.sh) пропущен: INITIAL_FILL_NO_SMOKE=1"
	echo "ТЕСТ ПРОЙДЕН"
	exit 0
fi

echo "== Шаг 4. Смок под созданным администратором =="
"$ROOT/scripts/smoke.sh" "$IB" || { echo "ТЕСТ НЕ ПРОЙДЕН: смок на заполненной базе"; exit 1; }
echo "ТЕСТ ПРОЙДЕН"
