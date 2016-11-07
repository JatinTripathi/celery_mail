#!/bin/bash

mkdir -p /var/run/celery
mkdir -p /var/log/celery

export PYTHONPATH='{PYTHONPATH}:/code'

python manage.py db upgrade

celery multi start w1 \
        -A gateway.celery \
        -l info \
        --pidfile=/var/run/celery/%n.pid \
        --logfile=/var/log/celery/%n%I.log

python gateway/server.py