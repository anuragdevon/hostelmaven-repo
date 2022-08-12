#!/bin/bash
source env/bin/activate
python src/manage.py makemigrations
python src/manage.py migrate
python src/manage.py runserver