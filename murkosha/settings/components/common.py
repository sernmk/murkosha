# -*- coding: utf-8 -*-

"""
Django settings for murkosha project.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from murkosha.settings.components import CONFIG, BASE_DIR

__author__ = 'sobolevn'

# Build paths inside the project like this: join(BASE_DIR, ...)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG['DJANGO_SECRET_KEY']

SITE_ID = 1


INSTALLED_APPS = (
    # Styling:
    'djangocms_admin_style',

    # Default apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    # Rate limiting:
    'axes',

    # Runtime settings:
    'constance',
    'constance.backends.database',

    # Django-CMS:
    'cms',
    'menus',
    'sekizai',
    'treebeard',

    # Custom:
    'landing_app',
)


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)


ROOT_URLCONF = 'murkosha.urls'

WSGI_APPLICATION = 'murkosha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': CONFIG['DJANGO_DATABASE_HOST'],
        'PORT': CONFIG['DJANGO_DATABASE_PORT'],
        'NAME': CONFIG['DJANGO_DATABASE_NAME'],
        'USER': CONFIG['DJANGO_DATABASE_USER'],
        'PASSWORD': CONFIG['DJANGO_DATABASE_PASSWORD'],
    }
}

# Security
# https://docs.djangoproject.com/en/1.10/ref/settings/#csrf-cookie-httponly

CSRF_COOKIE_HTTPONLY = True


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('ru', 'Русский'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    'locale/',
)


# Static files (CSS, JavaScript, Images).
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


# Templates:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Django-CMS:
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

                # Constance:
                'constance.context_processors.config',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]


# Media files
# Media-root is commonly changed in production (see development.py and production.py).

MEDIA_URL = '/media/'


# Django default authentication system.
# https://docs.djangoproject.com/en/1.10/topics/auth/

# AUTH_USER_MODEL = 'auth_app.SiteUser'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

SESSION_COOKIE_HTTPONLY = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Logging
# https://docs.djangoproject.com/en/1.10/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'server.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'server': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}


# Django Constance
# https://django-constance.readthedocs.io/en/latest

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {  # This is just an example:
    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
                       'The Universe, and Everything'),
}
