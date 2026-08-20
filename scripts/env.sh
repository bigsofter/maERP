#!/usr/bin/env bash
# Общее окружение для сборочных скриптов maERP (macOS).
# Подключается остальными скриптами через source.
set -euo pipefail

# Версия платформы, под которую собираем. По умолчанию — старшая из
# установленных сборок 8.5.1.*: ту же выбирает EDT, и расходиться с ней нельзя,
# иначе собранный CF и отлаживаемая конфигурация окажутся разной сборки.
if [ -z "${V8_VERSION:-}" ]; then
	V8_VERSION="$(ls -1 /opt/1cv8 2>/dev/null | grep -E '^8\.5\.1\.' | sort -V | tail -1)"
fi
V8_VERSION="${V8_VERSION:-8.5.1.1423}"
V8_DIR="/opt/1cv8/${V8_VERSION}"
V8="${V8_DIR}/1cv8"
IBCMD="${V8_DIR}/ibcmd"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_CF="${ROOT}/src/cf"          # EDT-проект основной конфигурации
SRC_EXT="${ROOT}/src/ext"        # EDT-проекты расширений
BUILD="${ROOT}/build"            # всё сборочное, в git не попадает
IB_BUILD="${BUILD}/ib"           # временная база сборки
XML_OUT="${BUILD}/xml"           # XML-выгрузка конфигурации
DIST="${BUILD}/dist"             # готовые CF/CFU для поставки

# Воркспейс EDT держим вне репозитория, иначе Eclipse-мусор полезет в git.
EDT_WS="${EDT_WS:-$HOME/EDT/ws-maERP}"
# Путь к 1cedtcli. Файл на месте, но без зарегистрированной в системе JVM
# не запускается — подробности в docs/EDT-SETUP.md.
EDT_VERSION="${EDT_VERSION:-1C_EDT 2026.1}"
EDT_CLI="${EDT_CLI:-$HOME/Library/Application Support/1C/1cedtstart/installations/$EDT_VERSION/1cedt.app/Contents/Eclipse/1cedtcli}"

# Общие ключи пакетного режима: без диалогов и без интерактивных сообщений.
V8_BATCH=(/DisableStartupDialogs /DisableStartupMessages)

[ -x "$V8" ] || { echo "Не найдена платформа: $V8" >&2; exit 1; }
mkdir -p "$BUILD"
