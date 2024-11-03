#!/bin/sh

sleep 20
python manage.py makemigrations
python manage.py migrate
python manage.py fill_db
python manage.py collectstatic --no-input
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
gunicorn --workers=2 mailing.service.wsgi:application --bind 0.0.0.0:8000