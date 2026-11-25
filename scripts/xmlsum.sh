#!/usr/bin/env bash
# Сумма XML-выгрузки конфигурации (build/xml): одна строка по содержимому и путям всех файлов. Хост пишет её в
# build/xml/.xmlsum, ВМ сверяет перед загрузкой в базу (scripts/vm-gate.sh, scripts/ib-sync.sh).
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
cd "$XML_OUT"
find . -type f ! -name .srchash ! -name .xmlsum -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 1 | shasum -a 1 | cut -d' ' -f1
