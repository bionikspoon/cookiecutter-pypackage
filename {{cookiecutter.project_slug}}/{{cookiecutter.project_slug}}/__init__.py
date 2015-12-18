#!/usr/bin/env python
# coding=utf-8
"""
==============
{{ cookiecutter.project_slug }}
==============

{{ cookiecutter.project_short_description }}

"""
from __future__ import absolute_import
import logging

from ._compat import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'
