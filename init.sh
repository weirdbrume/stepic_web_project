#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start

sudo pip3 install pymysql

cd /home/box/web/ask
sudo bash /home/box/web/ask/create_db.sh
sudo python3 manage.py makemigrations qa
sudo python3 manage.py migrate qa

sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo bash /home/box/web/ask/gunicorn_start.sh