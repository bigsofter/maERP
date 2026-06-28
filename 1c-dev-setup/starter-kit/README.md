# Стартовый комплект для 1С-проекта

Скопируй эти файлы в корень **отдельного** Git-репозитория конфигурации 1С (не в Go-проект maERP) и доработай пути.

## Что куда

| Файл в комплекте | Куда положить | Действие |
|---|---|---|
| `CLAUDE.md` | корень репо | как есть — правила для Claude Code |
| `mcp.json.example` | корень репо → **`.mcp.json`** | переименовать, убрать комментарии, вписать пути |
| `vscode-templates/extensions.json` | **`.vscode/extensions.json`** | переименовать папку в `.vscode` |
| `vscode-templates/settings.json` | **`.vscode/settings.json`** | вписать путь к Java и к JAR BSL LS |
| `.bslls.json` | корень репо | настройки диагностик линтера |
| `.gitignore` | корень репо | как есть |
| `.gitattributes` | корень репо | нормализация строк + бинарники 1С |
| `.editorconfig` | корень репо | стиль (табы в .bsl) |
| `scripts/dump-from-base.bat` | Windows-сервер | первичная выгрузка из живой базы |
| `scripts/build-and-deploy.bat` | Windows-сервер | сборка .cf + деплой test/prod |
| `scripts/lint.sh` | корень репо (Mac) | прогон BSL Language Server |

## Быстрый старт

```bash
# 1) создать репозиторий 1С-конфигурации (отдельно от maERP)
mkdir -p ~/Documents/Dev/1c-project && cd ~/Documents/Dev/1c-project
git init

# 2) скопировать сюда содержимое starter-kit (с переименованием dot-файлов/папок)
#    .vscode/, .mcp.json, CLAUDE.md, .bslls.json, .gitignore, .gitattributes, .editorconfig

# 3) скачать инструменты
mkdir -p ~/tools
#  - bsl-language-server-*-exec.jar  -> ~/tools/
#  - mcp-bsl-context-*.jar           -> ~/tools/   (alkoleft, MCP платформы)
#  - mcp-1c (бинарь feenlace)        -> ~/tools/   (опционально)

# 4) сделать lint.sh исполняемым
chmod +x scripts/lint.sh
```

Дальше — по основному руководству `../README-1C-DEV.md`.

## Заглушки, которые надо заменить

- `8.3.25.XXXX` → реальная версия платформы.
- `/Users/ivan-gurkin/tools/...` → реальные пути к JAR/бинарникам.
- `/opt/1cv8/x86_64/8.3.25.XXXX` → путь установки платформы 1С на Mac.
- `1c-server\prod_base`, `Администратор`, `ЗАМЕНИ_МЕНЯ` → реальные строки подключения и креды (креды — через секреты/переменные окружения, не в Git).
