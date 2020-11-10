"""
Django settings for together project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import mimetypes
from app.processors import global_processor

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import normpath, join

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


DOMAIN = 'together.com'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 5 * 60
SESSION_SAVE_EVERY_REQUEST = True


# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']
mimetypes.add_type("text/css", ".css", True)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'crispy_forms',
    'bootstrap4',
    'social_django',
    'app',
    'sass_processor',
    'rest_framework'
]

BOOTSTRAP4 = {
    'include_jquery': True,
}

ROOT_URLCONF = 'together.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'app/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'app.processors.global_processor.global_vars'
            ],
        },
    },
]

WSGI_APPLICATION = 'together.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "OPTIONS": {
            "options": "-c search_path=" + os.environ.get("DB_SCHEMA", "together")
        },
        "HOST": os.environ.get('DB_HOSTNAME'),
        "PORT": os.environ.get('DB_PORT', "5432"),
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USERNAME'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/



# Localization

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Tegucigalpa'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': "{}/together.log".format(os.path.dirname(BASE_DIR)),
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'together': {
            'handlers': ['file', 'console'],
            'level': os.getenv('TOGETHER_LOG_LEVEL', 'DEBUG'),
            'formatter': 'verbose',
        },
    },
}

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

AUTHORIZE_HEADER = 'Authorization'

HOME_PATH = '/'
USER_LOGIN_URL = '/login'
LOGIN_URL = '/super/login'
LOGIN_REDIRECT_URL = '/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
