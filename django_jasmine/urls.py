import os

from django.conf.urls.defaults import *
from django.conf import settings

from views import run_tests

static_root = os.path.join(os.path.dirname(__file__), 'static')
jasmine_version = "jasmine-1.1.0.rc1"


urlpatterns = patterns('django.views',
    url(r'^tests/(?P<path>.*)$', 'static.serve', {
        'document_root': os.path.join(settings.JASMINE_TEST_DIRECTORY, "spec"),
    }, name='jasmine_test'),
    url(r'^src/(?P<path>.*)$', 'static.serve', {
        'document_root': os.path.join(settings.JASMINE_TEST_DIRECTORY, "src"),
    }, name='jasmine_src'),
    url(r'^jasmine.js', 'static.serve', {
        'document_root': static_root,
        'path': '%s/jasmine.js' % jasmine_version,
    }, name='jasmine_js'),
    url(r'^jasmine-html.js', 'static.serve', {
        'document_root': static_root,
        'path': '%s/jasmine-html.js' % jasmine_version,
    }, name='jasmine_html_js'),
    url(r'^jasmine.css', 'static.serve', {
        'document_root': static_root,
        'path': '%s/jasmine.css' % jasmine_version,
    }, name='jasmine_css'),
    url('^(?P<path>.*)$', run_tests, name='jasmine_test_overview'),
)
