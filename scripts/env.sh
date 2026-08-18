#!/usr/bin/env bash
# Общее окружение для сборочных скриптов maERP (macOS).
# Подключается остальными скриптами через source.
set -euo pipefail

# Версия платформы, под которую собираем. Переопределяется переменной окружения.
V8_VERSION="${V8_VERSION:-8.5.1.1150}"
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
# Путь к 1cedtcli. Заполнить после установки EDT (см. docs/EDT-SETUP.md).
EDT_CLI="${EDT_CLI:-}"

# Общие ключи пакетного режима: без диалогов и без интерактивных сообщений.
V8_BATCH=(/DisableStartupDialogs /DisableStartupMessages)

[ -x "$V8" ] || { echo "Не найдена платформа: $V8" >&2; exit 1; }
mkdir -p "$BUILD"
