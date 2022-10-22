#!/usr/bin/env bash

apt update
apt install -y git python3 python3-pip python-is-python3 python3.10-venv
cd JCBDemo
python -m venv venv
bash venv/bin/activate
python -m pip install -r requirements.txt
python main.py
