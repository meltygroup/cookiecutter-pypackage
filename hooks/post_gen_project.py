import os
from subprocess import check_output

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def run(command):
    print(command)
    check_output(command.split())


if "{{ cookiecutter.type }}" == "application":
    os.remove("setup.py")
    os.chdir(PROJECT_DIRECTORY)
    run("git init")
    run("python3 -m venv venv")
    run("venv/bin/python -m pip install -U pip")
    run("venv/bin/python -m pip install pip-tools")
    run("venv/bin/pip-compile requirements.in")
    run("venv/bin/pip-compile requirements-dev.in")
    run("venv/bin/python -m pip install -r requirements-dev.txt")
    run("git add .")
    run("git commit -m Initial")
else:
    os.remove("requirements.in")
    os.remove("requirements-dev.in")
