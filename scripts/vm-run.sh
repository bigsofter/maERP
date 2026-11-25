#!/usr/bin/env bash
# Исполняется ВНУТРИ ВМ, в её локальной копии проекта (вызывает scripts/vm-gate.sh на хосте по ssh): окружение для
# скриптов 1С и запуск команды в корне проекта с журналом.
# Использование (в ВМ): scripts/vm-run.sh <журнал> <команда> [аргументы...]
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$1"; shift
# ifconfig (/sbin) нужен платформе для привязки программной лицензии; python3 - из Homebrew ВМ.
export PATH="/opt/homebrew/bin:/usr/sbin:/sbin:/usr/bin:/bin"
# Пароли - из файла с правами 600, который кладёт хост: в командной строке их нет.
set -a
source "$ROOT/build/vm/secrets.env"
set +a
cd "$ROOT"
"$@" > "$LOG" 2>&1
RC=$?
echo "rc=$RC" >> "$LOG"
exit $RC
