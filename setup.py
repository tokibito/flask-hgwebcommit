#!/usr/bin/env python
#:coding=utf-8:

from setuptools import setup, find_packages
 
setup (
    name='hgwebcommit',
    version='0.2',
    description='web based commit tool for mercurial',
    author='Shinya Okano',
    author_email='tokibito@gmail.com',
    url='http://bitbucket.org/tokibito/flask-hgwebcommit/',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    test_suite='tests',
)
