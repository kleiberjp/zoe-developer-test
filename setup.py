#!/usr/bin/env python

from setuptools import setup

setup(
    name='zoetest',
    version='1.0',
    description='web/rest servcies for knowledge test Full Stack Developer Zoetest',
    author='Kleiber Jose Perez',
    author_email='kleiberjp@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django==1.8.4',
        'psycopg2',
        'requests',
        'djangorestframework',
        'markdown',
        'django-filter',
        'django-suit',
        'django-rest-auth',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
