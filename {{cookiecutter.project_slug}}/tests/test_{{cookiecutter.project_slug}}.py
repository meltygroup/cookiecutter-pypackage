# -*- coding: utf-8 -*-

"""
    Tests for the `/{{ cookiecutter.project_slug }}.py` module.
"""
{% if cookiecutter.project_type == "package" %}
from unittest.mock import patch
import logging
import sys

import {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} as app


def test_package(capfd):
    """
        Test the output of the program.
    """
    logging.raiseExceptions = False
    with patch.object(sys, "argv", ['{{ cookiecutter.project_slug }}.py']):
        app.main()
    out, err = capfd.readouterr()
    assert "{{ cookiecutter.project_slug }} version {{ cookiecutter.project_version }}" in out
    assert err == ""


def test_package_with_verbose(capfd):
    """
        Test the output of the program with verbose mode.
    """
    logging.raiseExceptions = False
    app.main(["-v"])
    out, err = capfd.readouterr()
    assert "Hello world, verbose mode." in out
    assert err == ""
{% else %}
import {{ cookiecutter.project_slug }}


def test_module():
    """
        Test the output of 2 * 2.
    """
    assert {{ cookiecutter.project_slug }}.two_by_two() == 4
{% endif %}