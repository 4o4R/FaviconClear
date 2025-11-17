@echo off
setlocal
set "SCRIPT=%~dp0clear_favicon_cache.py"

echo Running favicon cache cleaner...

rem Try common Python launchers/interpreters in order; script enforces min version (2.7+)
py -3 "%SCRIPT%" 2>nul && goto :done
py -2 "%SCRIPT%" 2>nul && goto :done
py "%SCRIPT%" 2>nul && goto :done
python3 "%SCRIPT%" 2>nul && goto :done
python "%SCRIPT%" 2>nul && goto :done

echo.
echo Could not run Python. Please install Python from https://www.python.org/downloads/windows/
echo (check "Add Python to PATH"), then double-click run_cleaner.bat again.
pause
exit /b 1

:done
echo.
echo Done. Check above for details.
pause
endlocal
