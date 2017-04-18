# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.
Include other URLConfs from external apps using method include().

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from cms.sitemaps import CMSSitemap


__author__ = 'sobolevn'


admin.autodiscover()

urlpatterns = i18n_patterns(
    # django-admin:
    url(r'^admin/', include(admin.site.urls)),

    # text and xml static files:
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='txt/robots.txt',
        content_type='text/plain'
    )),
    url(r'^humans\.txt$', TemplateView.as_view(
        template_name='txt/humans.txt',
        content_type='text/plain'
    )),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),

    url(r'^crossdomain\.xml$', TemplateView.as_view(
        template_name='txt/crossdomain.xml',
        content_type='application/xml'
    )),

    # django-cms:
    url(r'^', include('cms.urls')),
)

# Customize default error views:
# https://docs.djangoproject.com/en/1.7/topics/http/views/#customizing-error-views

# handler400 = 'your_app.views.error_handler'
# handler403 = 'your_app.views.error_handler'
# handler404 = 'your_app.views.error_handler'
# handler500 = 'your_app.views.error_handler'


# This urlconf is for development use only:
if settings.DEBUG:

    # Media files serving:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
