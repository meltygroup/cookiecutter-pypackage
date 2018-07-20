# -*- coding: utf-8 -*-

"""
    Entry point of the application.
"""

from argparse import ArgumentParser
import logging
import sys

import {{ cookiecutter.project_slug }}.logger as logger


def main(program_args=None):
    """
        Main entry point of the program

        :param program_args: Arguments of the program (defaults to sys.argv)
        :type program_args: list of str
    """
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="enable debug logs",
    )

    if program_args is None:
        program_args = sys.argv[1:]

    args = parser.parse_args(program_args)
    level = logging.INFO

    if args.verbose:
        level = logging.DEBUG

    log = logger.get_logger("{{ cookiecutter.project_slug }}", level=level)
    log.info("{{ cookiecutter.project_slug }} version {{ cookiecutter.project_version }}")
    log.debug("Hello world, verbose mode.")
