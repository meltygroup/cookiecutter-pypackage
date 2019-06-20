"""Entry point of the application.
"""

import argparse
import logging
import sys


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.
    """

    parser = argparse.ArgumentParser(description="Please change me.")
    parser.add_argument(
        "--version", action="version", version="{{ cookiecutter.project_version }}"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity, use -vv to see warnings, "
        "-vvv for info and -vvvv for debug.",
    )
    parser.add_argument(
        "-q", "--quiet", action="count", default=0, help="Decrease verbosity."
    )
    args = parser.parse_args()
    args.loglevel = 10 * (5 - args.verbose + args.quiet)
    return args


def main():
    """Main entry point of the program.
    """
    args = parse_args()
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stderr,
        level=args.loglevel,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.debug("Hello")
    logging.info("Hello")
    logging.warning("Hello")
    logging.error("Hello")
    logging.critical("Hello")
