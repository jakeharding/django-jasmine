from django.conf import settings


DEFAULT_JASMINE_TAG = 'v1.3.1'

DEFAULT_JASMINE_VERSION = getattr(settings, 'DEFAULT_JASMINE_VERSION', DEFAULT_JASMINE_TAG)

