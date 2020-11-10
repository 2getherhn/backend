from together.settings.default import *
import os

DEBUG = True

TIME_ZONE = 'America/Los_Angeles'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USERNAME'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": os.environ.get('DB_HOSTNAME'),
        "PORT": "5432",
    }
}

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
