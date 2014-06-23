#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages


META_DATA = dict(
    name='django-jasmine',
    version='0.4.1',
    description='Jasmine Javascript testing integration for Django.',
    long_description=open('README.rst').read(),
    author='Jonathan McCoy',
    author_email='modelsolutions@gmail.com',
    maintainer='Adrien Lemaire',
    maintainer_email='adrien.lemaire@gmail.com',
    url='https://github.com/Aquasys/django-jasmine',
    keywords='django javascript test',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=['Django>=1.3', ],
    packages=find_packages(exclude=["example", ]),
    include_package_data=True,
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**META_DATA)
