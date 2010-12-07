#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django-jasmine',
    version='0.1',
    description='Jasmine Javascript testing integration for Django.',
    long_description=open('README.md').read(),
    author='Jonathan McCoy',
    author_email='modelsolutions@gmail.com',
    url='http://github.com/movity/django-jasmine',
    packages=[
        'django_jasmine',
    ],
    package_data={
        'django_jasmine': ['templates/jasmine/*', 'media/jasmine-1.0.1/*'],
    },
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: JavaScript',
                 'Topic :: Software Development :: Testing'],
)
