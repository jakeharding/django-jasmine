==============
django-jasmine
==============

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

*See the example directory for more information.*


Template
========

If you wish to modify the jasmine index template for any reason (e.g. add a new
jasmine reporter), you can create a jasmine/index.html template as follow::

    {% extends "jasmine/base.html" %}

    {% block jasmine_extra %}
        {# If you want to extend the default jasmineEnv config #}
    {% endblock %}

    {% block jasmine %}
        {# If you wish to rewrite the whole html runner script #}
    {% endblock %}


*Read templates/jasmine/base.html for the default config*

Several versions of jasmine will be kept for retro-compatibility. You can
override jasmine/base.html, and call for a specific version of jasmine (default
to jasmine-latest, a symlink to the latest version)


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


Todo
====

1. Write django tests for this app
2. Add headless testing environments (e.g jasmine-headless-webkit or Zombie.js)
3. Add Growl/notifyd notifications
4. Rewrite the view to be class-based
5. Add more settings for more flexibility

Versions
========

The Pypi django-jasmine version 0.3 includes:

* jasmine 1.1.0.rc1
* jasmine-jquery 1.3.1


license
=======

Copyright (c) 2010 Movity, Inc
Licensed new-style BSD, also containing Jasmine, which is licensed MIT. See
LICENSE file for more information.
