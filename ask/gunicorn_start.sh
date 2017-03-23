#!/usr/bin/env bash
# sudo gunicorn --bind=0.0.0.0:8080 hello:app
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000