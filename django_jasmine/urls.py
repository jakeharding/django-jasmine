import os
import django

if django.VERSION >= (1, 5):
    from django.conf.urls import patterns, url
else:
    from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from .views import DjangoJasmineView

static_root = settings.STATIC_ROOT


urlpatterns = [
    url(r'^tests/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.JASMINE_TEST_DIRECTORY, "spec"),
    }, name='jasmine_test'),
    url(r'^src/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.JASMINE_TEST_DIRECTORY, "src"),
    }, name='jasmine_src'),
    url(r'^fixtures/(?P<path>.*)$', serve, {
        'document_root': os.path.join(
            settings.JASMINE_TEST_DIRECTORY, "fixtures",
        ),
    }, name='jasmine_fixtures'),
    url('^(?P<version>.*)$', DjangoJasmineView.as_view(), name='jasmine_test_overview'),
]
