#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation
-------------

The full documentation is at https://{{ cookiecutter.project_slug }}.readthedocs.org.
"""

import os
import sys
import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.test import test as TestCommand

<<<<<<< a5beebee9ff0245192fdb9a46e238c6ffa3bfda0
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

=======
>>>>>>> add pytest class in setup.py and cleanup

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        import sys
        errno = pytest.main(self.test_args)
        sys.exit(errno)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# TODO: put package requirements here
requirements = []

# TODO: put package test requirements here
test_requirements = ['pytest', 'mock']

setup(  # :off
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + __doc__ + '\n\n' + history,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=[
        '{{ cookiecutter.project_slug }}',
    ],
    package_dir={'{{ cookiecutter.project_slug }}':
                 '{{ cookiecutter.project_slug }}'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    cmdclass={'test': PyTest},
    keywords='{{ cookiecutter.project_slug }} {{ cookiecutter.full_name }}',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)  # :on
