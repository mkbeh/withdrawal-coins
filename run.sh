#!/usr/bin/env bash

sudo apt install python-pip
cd withdrawal-cons
pip install -r requirements.txt
python withdrawal_coins.py