# -*- coding: utf-8 -*-

import os
import shutil

if "{{ cookiecutter.project_type }}" == "package":
    os.remove("{{ cookiecutter.project_slug }}.py")
else:
    shutil.rmtree("{{ cookiecutter.project_slug }}")
    os.remove("tests/test_logger.py")

if "{{ cookiecutter.has_docs }}" == "n":
    shutil.rmtree("docs")