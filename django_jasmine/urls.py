from django.conf.urls.defaults import *
from django.conf import settings
import os

media_root = os.path.join(os.path.dirname(__file__), 'media')
urlpatterns = patterns('',
    url(r'^tests/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.JASMINE_TEST_DIRECTORY+'/spec/',
    }, name='jasmine_test'),
    url(r'^jasmine/jasmine.js', 'django.views.static.serve', {
        'document_root': media_root, 'path': 'jasmine-1.0.1/jasmine.js',
    }, name='jasmine_js'),
    url(r'^jasmine/jasmine-html.js', 'django.views.static.serve', {
        'document_root': media_root, 'path': 'jasmine-1.0.1/jasmine-html.js',
    }, name='jasmine_html_js'),
    url(r'^jasmine/jasmine.css', 'django.views.static.serve', {
        'document_root': media_root, 'path': 'jasmine-1.0.1/jasmine.css',
    }, name='jasmine_css'),
    url('^(?P<path>.*)$', 'django_jasmine.views.run_tests',
        name='jasmine_test_overview'),
)
