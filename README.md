django-jasmine
============

django-jasmine integrates the [Jasmine Javascript testing framework][1] with [Django][2].  Jasmine is a behavior-driven development framework for testing your JavaScript code. It does not depend on any other JavaScript frameworks. It does not require a DOM. And it has a clean, obvious syntax so that you can easily write tests.

  [1]: http://pivotal.github.com/jasmine/
  [2]: http://www.djangoproject.com/

installation
============

 1. pip install django-jasmine
 2. Add 'django_jasmine' to your settings.INSTALLED_APPS.
 3. Add settings.JASMINE_TEST_DIRECTORY, containing the path to your javascript jasmine test files.  Files.json should be in this directory and all test files should be in settings.JASMINE_TEST_DIRECTORY + '/spec' *
 4. Add all Javascript files (including jQuery, and any other libraries) to files.json
 5. Add a urlconf to include('django_jasmine.urls').
 6. Visit the URL you've included in your urlconf to display Jasmine test results.

*See the example directory for more information.*

debug
=====

If you encounter some errors that isn't obvious to debug, you can add
"django_jasmine" to your loggers.

todo
====

 1. Write django tests for this app
 2. Add headless testing environments (e.g jasmine-headless-webkit or Zombie.js)
 3. Add Growl/notifyd notifications
 4. Rewrite the view to be class-based
 5. Refactorize urls for something prettier

license
=======

Copyright (c) 2010 Movity, Inc
Licensed new-style BSD, also containing Jasmine, which is licensed MIT. See LICENSE file for more information.
