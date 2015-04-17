#!/usr/bin/env python
# coding=utf-8

"""
test_{{ cookiecutter.repo_name }}
----------------------------------

Tests for ``{{ cookiecutter.repo_name }}`` module.
"""
import pytest


@pytest.fixture
def {{ cookiecutter.repo_name }}():
    from {{cookiecutter.repo_name}} import {{cookiecutter.repo_name}}

    mock_{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}()
    return mock_{{ cookiecutter.repo_name }}

def test_{{ cookiecutter.repo_name }}_properly_mocked({{ cookiecutter.repo_name }}):

    assert str({{ cookiecutter.repo_name }}) == "Success"
