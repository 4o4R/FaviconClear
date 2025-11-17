@echo off
setlocal
set "SCRIPT=%~dp0clear_favicon_cache.py"

if not exist "%SCRIPT%" (
  echo Could not find "%SCRIPT%".
  echo Please extract ALL files from the zip into the same folder, then run run_cleaner.bat again.
  pause
  exit /b 1
)

echo Running favicon cache cleaner...

rem Try common Python launchers/interpreters in order; script enforces min version (2.7+)
py -3 "%SCRIPT%" && goto :done
py -2 "%SCRIPT%" && goto :done
py "%SCRIPT%" && goto :done
python3 "%SCRIPT%" && goto :done
python "%SCRIPT%" && goto :done

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
