import os

BASE_PATH = os.path.dirname(__file__)

QUNIT_TEST_DIRECTORY = os.path.join(BASE_PATH, 'qunit_tests')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'example.urls'

INSTALLED_APPS = (
    'django_qunit',
)
