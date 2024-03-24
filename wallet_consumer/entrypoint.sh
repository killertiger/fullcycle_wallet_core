#!/bin/bash

python manage.py migrate && python manage.py loaddata fixtures/accounts.json && python manage.py runserver 0.0.0.0:3003