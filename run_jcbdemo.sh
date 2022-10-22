#!/usr/bin/env bash

apt update
apt install -y git python3 python3-pip python-is-python3 python3.10-venv
git clone https://github.com/SheljaRajan/JCBDemo.git
cd JCBDemo
python -m venv venv
bash venv/bin/activate
python -m pip install -r requirements.txt
sysctl -w net.ipv4.ip_forward=1
python main.py
