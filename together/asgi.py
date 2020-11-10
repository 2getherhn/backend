"""
ASGI config for 2GETHER project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

default_env = os.environ.get('ENVIRONMENT') if os.environ.get('ENVIRONMENT') else 'default'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "together.settings." + default_env)

application = get_asgi_application()

