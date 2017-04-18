# -*- coding: utf-8 -*-

"""
This file determines all the settings that must define the development server.
Basically this is a local file. It is excluded from the VCS by default.

SECURITY WARNING: don't run with debug turned on in production!
"""

import os

# Mind the proper import, use the right module!
from murkosha.settings.components.common import (
    BASE_DIR,
    TEMPLATES,
)

__author__ = 'sobolevn'


# Setting the development status:

DEBUG = True

FRONTEND_DEBUG = True

for template in TEMPLATES:
    template['OPTIONS']['debug'] = True


ALLOWED_HOSTS = []


# Network security and SSL:

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',

    # Uncomment next line and run 'runserver 0.0.0.0:8000' for production test:
    # '192.168.your.ip'
]

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False


# Static files:
# https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS = (
    # Adding frontend package managers in development:
    # os.path.join(BASE_DIR, 'node_modules'),
    # os.path.join(BASE_DIR, 'bower_components'),
)

# Adding STATIC_ROOT to collect static files via 'collectstatic'.
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Media files root:
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
