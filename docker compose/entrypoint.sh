#!/bin/bash
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --no-input
gunicorn stocks_products.wsgi:application --bind 0.0.0.0:8000
