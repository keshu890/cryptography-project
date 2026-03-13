@echo off
REM SimSecure Global Setup - Run as Administrator
REM This script installs SimSecure globally so you can use it from anywhere
REM
REM Usage: Right-click on install_global.bat and select "Run as Administrator"
REM
REM After running this, you can use from any directory:
REM   simsecure -ls
REM   simsecure password "test123"
REM   simsecure web https://example.com

echo =========================================
echo  SimSecure Global Installation
echo =========================================
echo.

REM Check if running as admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] ERROR: This script requires Administrator privileges!
    echo [!] Right-click and select "Run as Administrator"
    pause
    exit /b 1
)

echo [+] Admin privileges confirmed
echo.

REM Copy the batch file to System32
echo [*] Installing simsecure command globally...
copy "%~dp0simsecure.bat" "C:\Windows\System32\simsecure.bat"

if %errorLevel% equ 0 (
    echo [+] SUCCESS! SimSecure installed globally!
    echo.
    echo [+] You can now use simsecure from ANY directory:
    echo.
    echo     simsecure -ls
    echo     simsecure password "YourPassword#123"
    echo     simsecure web https://example.com
    echo     simsecure port example.com
    echo.
    echo [+] Test it:
    simsecure -ls
) else (
    echo [-] ERROR: Failed to install SimSecure
    echo [-] Please run this script as Administrator
)

pause
