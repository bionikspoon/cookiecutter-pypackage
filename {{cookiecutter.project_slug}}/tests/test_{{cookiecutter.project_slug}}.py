#!/usr/bin/env python
# coding=utf-8

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""
import pytest


@pytest.fixture
def {{ cookiecutter.project_slug }}():
    from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

    mock_{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}()
    return mock_{{ cookiecutter.project_slug }}


def test_{{ cookiecutter.project_slug }}_properly_mocked({{ cookiecutter.project_slug }}):
    assert str({{ cookiecutter.project_slug }}) == "Success"
