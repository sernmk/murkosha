# -*- coding: utf-8 -*-

"""
Settings for Django CMS.
"""
from django.utils.translation import gettext_lazy as _

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'ru',
            'hide_untranslated': False,
            'name': 'Русский',
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': 'English',
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = [
]

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    # Default:

    None: {
        'plugins': ['TextPlugin'],
        'excluded_plugins': ['InheritPlugin'],
    },
}
