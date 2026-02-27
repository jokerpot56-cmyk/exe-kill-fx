@echo off
setlocal

REM Build Kill FX Tool into a standalone Windows EXE using PyInstaller.
python -m pip install --upgrade pip
python -m pip install pyinstaller

pyinstaller --noconfirm --onefile --windowed --name kill-fx-tool kill_fx_tool.py

echo.
echo Build complete. EXE is located at: dist\kill-fx-tool.exe
endlocal
