# Kill FX Tool (EXE build)

This repo contains a Tkinter utility (`kill_fx_tool.py`) and a simple Windows build script (`build_exe.bat`) to package it as an EXE.

## Build EXE (Windows)

1. Install Python 3.10+.
2. Open `cmd` in this folder.
3. Run:

```bat
build_exe.bat
```

After build finishes, your executable will be at:

```text
dist\kill-fx-tool.exe
```

## Manual build command

If you prefer to run PyInstaller manually:

```bat
python -m pip install pyinstaller
pyinstaller --onefile --windowed --name kill-fx-tool kill_fx_tool.py
```
