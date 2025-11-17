@echo off
setlocal
set "SCRIPT=%~dp0clear_favicon_cache.py"

echo Running favicon cache cleaner...
python "%SCRIPT%" || py -3 "%SCRIPT%" || py "%SCRIPT%"
echo.
echo Done. Check above for details.

pause
endlocal
