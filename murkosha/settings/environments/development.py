# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import,unused-wildcard-import

"""
This file determines all the settings that must define the development server.
Basically this is a local file. It is excluded from the VCS by default.

SECURITY WARNING: don't run with debug turned on in production!
"""

# Mind the proper import, use the right module!

from murkosha.settings.environments.testing import *  # NOQA
from murkosha.settings.components import GlobalIPList

__author__ = 'sobolevn'


INTERNAL_IPS = GlobalIPList([
    '127.0.0.1',
    '192.168.0.*'

    # Uncomment next line and run 'runserver 0.0.0.0:8000' for production test:
    # '192.168.net.*'
])
