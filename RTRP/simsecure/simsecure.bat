@echo off
REM SimSecure - Professional Cybersecurity Command-Line Tool
REM This batch file allows simsecure to be called from anywhere
REM
REM Installation:
REM 1. Copy this file to C:\Windows\System32\ or add the folder containing this file to PATH
REM 2. Then use: simsecure -ls  (from any directory)
REM
REM Usage:
REM   simsecure -ls                              (List commands)
REM   simsecure password "YourPass#123"          (Test password)
REM   simsecure web https://example.com          (Scan website)
REM   simsecure port example.com                 (Scan ports)

python "C:\Programming\RTRP\simsecure\simsecure.py" %*
