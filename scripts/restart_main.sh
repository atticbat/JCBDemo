#!/usr/bin/env bash

ps -e | grep python | awk '{print $1}' | while read -r a; do kill -9 $a; done
python /JCBDemo/main.py
