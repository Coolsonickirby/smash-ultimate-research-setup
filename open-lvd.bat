@echo OFF

IF [%1]==[] (
    echo Usage^: open-lvd ^<ARC Path^>
) ELSE (
    yamlvd "%ULTIMATE_ARC_FOLDER%\%1" "tmp.yaml"
    nano tmp.yaml
    clear
)
