"""
WSGI config for rental project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import site
site.addsitedir('/home/shatan/django/venv/django1.6/lib/python-2.7/site-packages')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rental.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
