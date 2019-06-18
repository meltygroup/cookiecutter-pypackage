"""Tests for the `/{{ cookiecutter.project_slug }}.py` module.
"""
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
