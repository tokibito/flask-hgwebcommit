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
    install_requires=[
      'Flask>=0.6.1',
      'Flask-Babel>=0.6',
      'Flask-WTF>=0.5.2',
      'simplejson>=2.1.0',
      'mercurial>=1.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
)
