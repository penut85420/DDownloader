@echo off
pipenv run pyuic5 ddownloader\main_ui.ui -o ddownloader\main_ui.py --import . --resource-suffix ""
pipenv run pyrcc5 ddownloader\main_rc.qrc -o ddownloader\main_rc.py
