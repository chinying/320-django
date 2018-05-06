import os
from internportal.settings import DATABASES

DATABASES['default']['NAME'] = os.environ['DB_SCHEMA']
DATABASES['default']['USER'] = os.environ['DB_USER']
DATABASES['default']['PASSWORD'] = os.environ['DB_PASSWORD']
DATABASES['default']['HOST'] = os.environ['DB_HOST']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASS']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ['EMAIL_USER']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
