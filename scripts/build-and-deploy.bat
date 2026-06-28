@echo off
REM ============================================================
REM  Сборка .cf из исходников и деплой в тест/прод (Windows)
REM  Использование: build-and-deploy.bat test  |  build-and-deploy.bat prod
REM  Перед prod ОБЯЗАТЕЛЬНО делается бэкап и подразумевается окно обслуживания.
REM ============================================================

set V8="C:\Program Files\1cv8\8.3.25.XXXX\bin\1cv8.exe"
set USR=Администратор
set PWD=ЗАМЕНИ_МЕНЯ
set SRC=D:\repo\src
set BUILD_BASE=1c-server\build_base
set TEST_BASE=1c-server\test_base
set PROD_BASE=1c-server\prod_base
set OUT_CF=D:\build\app.cf
set BACKUP_DIR=D:\backups

set TARGET=%1
if "%TARGET%"=="" (echo Укажи цель: test или prod & exit /b 1)

echo === 1. Сборка .cf из исходников ===
%V8% DESIGNER /S "%BUILD_BASE%" /N %USR% /P %PWD% /LoadConfigFromFiles "%SRC%" /DumpCfg "%OUT_CF%" /DisableStartupDialogs
if errorlevel 1 goto :err

if "%TARGET%"=="test" set DB=%TEST_BASE%
if "%TARGET%"=="prod" set DB=%PROD_BASE%

if "%TARGET%"=="prod" (
  echo === Бэкап прод перед обновлением ===
  %V8% DESIGNER /S "%PROD_BASE%" /N %USR% /P %PWD% /DumpIB "%BACKUP_DIR%\prod_%date:~-4%-%date:~3,2%-%date:~0,2%.dt" /DisableStartupDialogs
  if errorlevel 1 goto :err
  echo ВНИМАНИЕ: убедись, что включена блокировка сеансов / монопольный режим.
)

echo === 2. Загрузка .cf и обновление БД (%DB%) ===
%V8% DESIGNER /S "%DB%" /N %USR% /P %PWD% /LoadCfg "%OUT_CF%" /UpdateDBCfg -Server /DisableStartupDialogs
if errorlevel 1 goto :err

echo Деплой в %TARGET% завершён.
goto :eof

:err
echo ОШИБКА деплоя. Останавливаемся.
exit /b 1
