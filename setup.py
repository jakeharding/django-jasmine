#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages


META_DATA = dict(
    name='django-jasmine',
    version='0.3.2.3',
    description='Jasmine Javascript testing integration for Django.',
    long_description=open('README.rst').read(),
    author='Jonathan McCoy',
    author_email='modelsolutions@gmail.com',
    maintainer='Adrien Lemaire',
    maintainer_email='adrien.lemaire@gmail.com',
    url='https://github.com/Fandekasp/django-jasmine',
    keywords='django javascript test',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=['Django>=1.3', 'webassets', 'gears'],
    packages=find_packages(exclude=["example", ]),
    include_package_data=True,
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**META_DATA)
