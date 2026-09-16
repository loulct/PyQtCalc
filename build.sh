#!/bin/bash
set -e

uv run pyinstaller --noconfirm --onedir --windowed --name=Calc src/__main__.py

wget -v https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy-x86_64.AppImage

mkdir -p AppDir/usr/bin
cp -r dist/Calc/* AppDir/usr/bin/

touch calc.svg

./linuxdeploy-x86_64.AppImage --appdir=AppDir -d calc.desktop -i calc.svg --output appimage
