@echo off
setlocal
set "SCRIPT=%~dp0clear_favicon_cache.py"

echo Running favicon cache cleaner...

rem Prefer the Python Launcher (py) with Python 3
py -3 "%SCRIPT%" 2>nul && goto :done

rem Next, try python3 if available
python3 "%SCRIPT%" 2>nul && goto :done

rem Last resort: only run with python if it is Python 3
python -c "import sys; sys.exit(sys.version_info < (3,7))" 2>nul && python "%SCRIPT%" && goto :done

echo.
echo Could not run with Python 3.
echo Please install Python 3 from https://www.python.org/downloads/windows/
echo (check "Add Python to PATH"), then double-click run_cleaner.bat again.
pause
exit /b 1

:done
echo.
echo Done. Check above for details.
pause
endlocal
