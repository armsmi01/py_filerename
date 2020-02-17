:: pyinstaller batch script to create executable from python source code with the following parameters
:: onefile - executable will be a single file
:: icon - custom icon must be defined
:: path - saved to executable folder
@echo off
color A
cls
SET prog_name=Month-End File Rename
SET src_file=file_rename.py
SET icon_file=preview.ico
title Pyinstaller for %prog_name%
echo Creating %prog_name% executable for current system
pause

:: COMMENT OUT PYINSTALLER SELECTION FOR THE NUMBER OF STEPS BACK TO ROOT
:: depth of file structure matters
:: Can be 3 or 4 steps (4 more common)

:: 3 = ..\\..\\..\\executable\\
:: 3 steps, eg C:\Programs\python\src\JDE Explorer
:: Clear old data if present
IF EXIST "..\\..\\..\\executable\\%prog_name%" rmdir /s /q "..\\..\\..\\executable\\%prog_name%"
pyinstaller --onefile --name "%prog_name%" --distpath "..\\..\\..\\executable\\%prog_name%\\dist" --workpath "..\\..\\..\\executable\\%prog_name%\\build" --icon="..\\..\\..\\icons\\%icon_file%" %src_file%
:: copy bin folder if present
::IF EXIST bin echo d | xcopy bin "..\\..\\..\\executable\\%prog_name%\\bin" /E
:: copy data folder if present
::IF EXIST data echo d | xcopy data "..\\..\\..\\executable\\%prog_name%\\data" /E
:: Moves executable to direct folder location
::move "..\\..\\..\\executable\\%prog_name%\\dist\\%prog_name%.exe" "..\\..\\..\\..\\executable\\%prog_name%\\%prog_name%.exe"
:: Removes dist folder
::rmdir /s /q "..\\..\\..\\executable\\%prog_name%\\dist"
:: Removes build folder
::rmdir /s /q "..\\..\\..\\executable\\%prog_name%\\build"

:: 4 = ..\\..\\..\\..\\executable\\
:: 4 steps, eg C:\Programs\python\src\Web Interaction\FDW Mapping
:: Clear old data if present
:: IF EXIST "..\\..\\..\\..\\executable\\%prog_name%" rmdir /s /q "..\\..\\..\\..\\executable\\%prog_name%"
:: pyinstaller --onefile --name "%prog_name%" --distpath "..\\..\\..\\..\\executable\\%prog_name%\\dist" --workpath "..\\..\\..\\..\\executable\\%prog_name%\\build" --icon="..\\..\\..\\..\\icons\\%icon_file%" %src_file%
:: copy bin folder if present
:: IF EXIST bin echo d | xcopy bin "..\\..\\..\\..\\executable\\%prog_name%\\bin" /E
:: copy data folder if present
:: IF EXIST data echo d | xcopy data "..\\..\\..\\..\\executable\\%prog_name%\\data" /E
:: Moves executable to direct folder location
:: move "..\\..\\..\\..\\executable\\%prog_name%\\dist\\%prog_name%.exe" "..\\..\\..\\..\\executable\\%prog_name%\\%prog_name%.exe"
:: Removes dist folder
:: rmdir /s /q "..\\..\\..\\..\\executable\\%prog_name%\\dist"
:: Removes build folder
:: rmdir /s /q "..\\..\\..\\..\\executable\\%prog_name%\\build"

:: Removes files/folders created during MAKE process
rmdir /s /q __pycache__
del *.spec

