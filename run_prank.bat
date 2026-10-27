@echo off
cd /d "%~dp0"
start "" pyw fake_virus.py
if errorlevel 1 py fake_virus.py
