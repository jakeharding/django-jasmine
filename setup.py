#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages


META_DATA = dict(
    name='django-jasmine',
    version='0.5.0',
    description='Jasmine Javascript testing integration for Django.',
    long_description=open('README.rst').read(),
    author='Jonathan McCoy',
    author_email='modelsolutions@gmail.com',
    maintainer='Jake Harding',
    maintainer_email='jacobeharding@gmail.com',
    url='https://github.com/jakeharding/django-jasmine',
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
    install_requires= ['Django>=1.8', ],
    packages=find_packages(exclude=["example_project", "tests"]),
    include_package_data=True,
    zip_safe=False,
    license='BSD'
)


if __name__ == "__main__":
    setup(**META_DATA)
