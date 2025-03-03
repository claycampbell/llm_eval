@echo off
pip install -r requirements.txt
set FLASK_APP=simple.py
python -m flask run