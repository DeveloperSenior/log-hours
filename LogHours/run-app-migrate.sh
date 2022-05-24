#!/bin/sh

pip install -r requirements.txt
python manage.py flush --no-input
python manage.py migrate
python manage.py runserver

exec "$@"