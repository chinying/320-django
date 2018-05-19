#!/bin/bash

# declaring env variables
export SERVER_TYPE="PROD"

export DJANGO_SECRET_KEY=""

export DB_SCHEMA=""
export DB_USER=""
export DB_PASSWORD=""
export DB_HOST=""

export EMAIL_HOST=""
export EMAIL_PORT=
export EMAIL_USER=""
export EMAIL_PASS=""

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn internportal.wsgi:application \
    --bind 0.0.0.0:5000 \
    --workers 3