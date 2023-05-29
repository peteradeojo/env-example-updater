#!/usr/bin/sh

rm -rf build dist

pyinstaller -F main.py -n envUpdater --noconsole

mv dist/envUpdater envUpdater

rm -rf build dist

