#!/usr/bin/env bash

rm -rf ./volumes/jcb_static/venv
rm -rf ./volumes/jcb_dynamic/venv
docker stop jcb_dynamic
docker stop jcb_static
