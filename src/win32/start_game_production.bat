@echo off
cd ..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set /P tteUsername="Username: "
set /P ttePassword="Password: "
set /P TTE_GAMESERVER="Gameserver (DEFAULT: 167.114.28.238): " || ^
set TTE_GAMESERVER=167.114.28.238

echo ===============================
echo Starting Toontown Evolution...
echo ppython: %PPYTHON_PATH%
echo Username: %tteUsername%
echo Gameserver: %TTE_GAMESERVER%
echo ===============================

%PPYTHON_PATH% -m toontown.toonbase.ClientStartProduction
pause
