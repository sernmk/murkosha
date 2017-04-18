# -*- coding: utf-8 -*-

"""
WSGI config for murkosha project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


__author__ = 'sobolevn'

# This setting should be available via heroku config:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'murkosha.settings')

# To enable SSL add extra environment variables:
# os.environ['wsgi.url_scheme'] = 'https'
# os.environ['HTTPS'] = 'on'

application = get_wsgi_application()
