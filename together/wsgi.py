"""
WSGI config for 2GETHER project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

default_env = os.environ.get('ENVIRONMENT') if os.environ.get('ENVIRONMENT') else 'default'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "together.settings." + default_env)

application = get_wsgi_application()
