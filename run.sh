#!/usr/bin/env bash

sudo git clone https://github.com/smartholdem/smartholdem-rpc.git
cd smartholdem-rpc
npm install
forever start server.js

sudo apt install python-pip
cd withdrawal-coins
pip install -r requirements.txt
sudo python withdrawal_coins.py
forever stop server.js