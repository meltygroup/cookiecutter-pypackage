import os
from subprocess import check_output

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if "{{ cookiecutter.type }}" == "application":
    os.remove("setup.py")
    os.chdir(PROJECT_DIRECTORY)
    check_output(["git", "init"])
    check_output(["python3", "-m", "venv", "venv"])
    check_output(["venv/bin/python", "-m", "pip", "install", "-U", "pip"])
    check_output(["venv/bin/python", "-m", "pip", "install", "pip-tools"])
    check_output(["venv/bin/pip-compile", "requirements.in"])
    check_output(["venv/bin/pip-compile", "requirements-dev.in"])
    check_output(["git", "add", "."])
    check_output(["git", "commit", "-m", "Initial commit."])
else:
    os.remove("requirements.in")
    os.remove("requirements-dev.in")
