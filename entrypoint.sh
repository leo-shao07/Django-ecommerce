#!/bin/bash
echo =========================
echo hi from entrypoint
echo =========================
python manage.py test shop
echo =========================
echo Running Django on the local host at http://127.0.0.1:8000 go check it out
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
