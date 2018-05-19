## Setup Instructions

### Database (PostgreSQL)
`ALTER ROLE internportal SET client_encoding TO 'utf8';`
`ALTER ROLE internportal SET default_transaction_isolation TO 'read committed';`
`ALTER ROLE internportal SET timezone TO 'UTC';`
`GRANT ALL PRIVILEGES ON DATABASE internportal TO internportal;  `

alternatively
```
$ psql internportal -c "GRANT ALL ON ALL TABLES IN SCHEMA public to internportal;"
$ psql internportal -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to internportal;"
$ psql internportal -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to internportal;"
```

### Django
### Add settings\_local.py in `internportal` dir
fill in where necessary
```
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True

EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

```

### Run migrations

`python manage.py migrate`

### Run app

`python manage.py runserver`

### Run Tests
`SERVER_TYPE=TEST pytest`

### SASS
sass compilation `sass --watch ./static/sass:./static/css --style compressed` (yet to write grunt / gulp for this)

## Production
`python manage.py collectstatic --noinput`

`docker build -t "fyp_production_caddy" .`

`./deploy.sh`

`docker-compose up -d`

## Credits
- [Django Cookiecutter](https://github.com/pydanny/cookiecutter-django), a lot of boilerplate was adapted from the generated code.
- [Flatly Bootstrap Theme](https://bootswatch.com/flatly/), made by [Thomas Park](https://thomaspark.co/), MIT licenced.