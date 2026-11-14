@echo off
title KSR TeleCRM Dashboard Updater
color 0b
echo ===================================================================
echo   KSR DATAVISION - TELECRM AUTOMATED DASHBOARD REFRESH
echo ===================================================================
echo.
echo Running automatic CSV/Excel data ingestion and dashboard rebuild...
echo.
python update_dashboard.py
echo.
echo ===================================================================
echo Done! Opening updated dashboard in your default browser...
echo ===================================================================
start "" "index.html"
pause
