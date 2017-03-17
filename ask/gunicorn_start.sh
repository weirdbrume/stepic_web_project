#!/usr/bin/env bash
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000