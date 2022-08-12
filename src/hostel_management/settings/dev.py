# Imports
from .base import *
import os

# DEBUG MODE (set it to "True" in dev mode)
DEBUG = True

# Allowed all local ports
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': int(os.environ['DB_PORT'])
    }
}
# netflixdemo
# Developement server 
WSGI_APPLICATION = "netflix.wsgi.application"
