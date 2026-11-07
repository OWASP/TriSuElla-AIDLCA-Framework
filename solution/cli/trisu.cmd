@echo off
setlocal
where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    py -3 "%~dp0tools\trisu-cli\trisu_validator.py" %*
) else (
    python "%~dp0tools\trisu-cli\trisu_validator.py" %*
)
exit /b %ERRORLEVEL%
