==============
django-jasmine
==============

###Pull requests and issues are welcome!

django-jasmine integrates the
`Jasmine Javascript testing framework <http://pivotal.github.com/jasmine/>`_
with `Django <http://www.djangoproject.com/>`_.  Jasmine is a behavior-driven
development framework for testing your JavaScript code. It does not depend on
any other JavaScript frameworks.  It does not require a DOM. And it has a
clean, obvious syntax so that you can easily write tests.

django-jasmine also integrates the
`jasmine-jquery <https://github.com/velesin/jasmine-jquery>`_ plugin, that
provides a set of custom matchers for jQuery framework and an API for handling
HTML fixtures in your specs.


Installation
============

1. pip install django-jasmine
2. Add 'django_jasmine' to your settings.INSTALLED_APPS.
3. Add settings.JASMINE_TEST_DIRECTORY, containing the path to your javascript
   jasmine test files.  Files.json should be in this directory and all test
   files should be in os.path.join(settings.JASMINE_TEST_DIRECTORY, 'spec') *
4. Makes sure you have properly defined a STATIC_URL.
5. Add all Javascript files (including jQuery, and any other libraries) to
   files.json
6. Add a urlconf to include('django_jasmine.urls').
7. Visit the URL you've included in your urlconf to display Jasmine test
   results.
8. Add a corresponding tag from the Jasmine github repo to specify a version of Jasmine to test with. Otherwise the latest tag, currently v2.4.1, is loaded.

*Jasmine is now loaded over cdn.rawgit.com.  A very obvious error message will appear if Jasmine isn't loaded correctly.*

*See the example directory for more information.*


Template
========

If you wish to modify the jasmine index template for any reason (e.g. add a new
jasmine reporter), you can create a jasmine/index.html template as follow::

    {% extends "jasmine/base.html" %}

    {% block jasmine_preload %}
        {# If you need to do any setup before dependencies in files.json are loaded (like define app namespace) #}
    {% endblock %}

    {% block jasmine_extra %}
        {# If you want to extend the default jasmineEnv config #}
    {% endblock %}

    {% block jasmine %}
        {# If you wish to rewrite the whole html runner script #}
    {% endblock %}


*Read templates/jasmine/base.html for the default config*

Fixtures
========

jasmine-jquery allowing to add fixtures, you can set them in
os.path.join(settings.JASMINE_TEST_DIRECTORY, 'fixtures'). Then in your spec::

    jasmine.getFixtures().fixturesPath = "/jasmine/fixtures/";
    loadFixtures("template.html")


Debug
=====

If you encounter some errors that isn't obvious to debug, you can add
"django_jasmine" to your loggers.


Integration with ./manage.py tests
==================================

To do so, I recommend using
`EnvJasmine <https://github.com/trevmex/EnvJasmine>`_, and use
`Fabric <http://docs.fabfile.org/en/1.3.3/index.html>`_ to run EnvJasmine after
running manage.py tests


Todo
====

1. Keep improving django tests
2. Add Growl/notifyd notifications
3. Add more settings for more flexibility i.e. make a symbolic constant for cdn url.
4. Thoroughly test fixtures and jasmine-jquery features.
5. Improve README.
6. Use a more specific pattern matcher for the version url. 


license
=======

Copyright (c) 2010 Movity, Inc
Licensed new-style BSD, also containing Jasmine, which is licensed MIT. See
LICENSE file for more information.
