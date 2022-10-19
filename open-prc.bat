@echo OFF

IF [%1]==[] (
    echo Usage^: open-prc ^<ARC Path^>
) ELSE (
    prickly "%ULTIMATE_ARC_FOLDER%\%1"
    clear
)
