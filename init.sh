#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo gunicorn --bind=0.0.0.0:8080 hello:app
cd /home/box/web/ask
sudo bash /home/box/web/ask/gunicorn_start.sh