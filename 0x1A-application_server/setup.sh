#!/usr/bin/bash

sudo apt-get -y update
sudo apt-get install -y nginx
sudo apt-get install -y python3-pip
pip install flask
pip install flask_cors
pip install sqlalchemy
sudo apt install -y net-tools
sudo apt-get install -y gunicorn
