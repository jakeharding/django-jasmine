def pytest_configure():
    from django.conf import settings

    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                               'NAME': ':memory:'}},
        SECRET_KEY='not very secret in tests',
        JASMINE_TEST_DIRECTORY='../example/jasmine/',
        STATIC_URL='/static/',
        ROOT_URLCONF='tests.urls',
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.staticfiles',
            'django_jasmine',
        ),
    )

    try:
        import django
        django.setup()
    except AttributeError:
        pass