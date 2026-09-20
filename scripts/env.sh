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
EDT_VERSION="${EDT_VERSION:-1C_EDT 2026.1}"
EDT_CLI="${EDT_CLI:-$HOME/Library/Application Support/1C/1cedtstart/installations/$EDT_VERSION/1cedt.app/Contents/Eclipse/1cedtcli}"

# 1cedtcli на macOS — исполняемый файл x86_64, и ему нужна JDK 17+ ТОЙ ЖЕ архитектуры.
# arm64-JDK (та, на которой работает BSL LS) не подходит: лаунчер падает с
# «JVM shared library ... does not contain the JNI_CreateJavaVM symbol», причём
# в stdout ничего не пишет — ошибка уходит в <EDT_WS>/.metadata/1cedtcli.log,
# а наружу виден только пустой вывод и rc=254. Ключа -vm у 1cedtcli нет,
# версия JVM берётся из JAVA_HOME/PATH, поэтому её задаём здесь.
# Автоопределение: первая x86_64-JDK из зарегистрированных в системе.
if [ -z "${EDT_JAVA_HOME:-}" ] && [ -x /usr/libexec/java_home ]; then
  EDT_JAVA_HOME="$(/usr/libexec/java_home -V 2>&1 | awk '/x86_64/ {sub(/.*" /, ""); print; exit}')"
fi
EDT_JAVA_HOME="${EDT_JAVA_HOME:-}"

# Общие ключи пакетного режима: без диалогов и без интерактивных сообщений.
V8_BATCH=(/DisableStartupDialogs /DisableStartupMessages)

[ -x "$V8" ] || { echo "Не найдена платформа: $V8" >&2; exit 1; }
mkdir -p "$BUILD"
