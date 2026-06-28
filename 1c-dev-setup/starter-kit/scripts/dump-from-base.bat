@echo off
REM ============================================================
REM  Выгрузка конфигурации из живой базы в файлы (Windows-сервер)
REM  Запускать на Windows, где установлена платформа 1С.
REM  Отредактируй переменные ниже под своё окружение.
REM ============================================================

set V8="C:\Program Files\1cv8\8.3.25.XXXX\bin\1cv8.exe"
set SRV=1c-server\prod_base
set USR=Администратор
set PWD=ЗАМЕНИ_МЕНЯ
set OUT_CF=D:\export\prod.cf
set OUT_SRC=D:\export\src

echo === Выгрузка в .cf ===
%V8% DESIGNER /S "%SRV%" /N %USR% /P %PWD% /DumpCfg "%OUT_CF%" /DisableStartupDialogs
if errorlevel 1 goto :err

echo === Выгрузка в XML-файлы (формат конфигуратора) ===
%V8% DESIGNER /S "%SRV%" /N %USR% /P %PWD% /DumpConfigToFiles "%OUT_SRC%" /DisableStartupDialogs
if errorlevel 1 goto :err

echo Готово. Перенеси %OUT_CF% и %OUT_SRC% на Mac.
goto :eof

:err
echo ОШИБКА выгрузки. Проверь путь к платформе, строку базы и пароль.
exit /b 1
