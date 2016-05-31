#!/usr/bin/env python
# coding=utf-8

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""
from pytest import fixture


@fixture
def boilerplate():
    from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import Boilerplate

    return Boilerplate()


def test_cookiecutter_automates_boilerplate(boilerplate):
    assert str(boilerplate) == "Success"
