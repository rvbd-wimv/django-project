#!/bin/bash
cd /opt/app/nightlife
python manage.py makemigrations m_api
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser --no-input
#python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 \
--forwarded-allow-ips="172.19.0.4" \
--access-logfile '-' \
--access-logformat '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' \
nightlife.wsgi