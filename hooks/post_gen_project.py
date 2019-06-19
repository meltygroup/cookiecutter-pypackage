import os
from subprocess import check_output

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def run(command):
    print(command)
    check_output(command.split())


os.chdir(PROJECT_DIRECTORY)

run("git init")
run("python3 -m venv venv")
run("venv/bin/python -m pip install -U pip")
run("venv/bin/python -m pip install pip-tools")

if "{{ cookiecutter.type }}" == "application":
    # An app uses a requirements.txt but no setup.py
    os.remove("setup.py")
    run("venv/bin/pip-compile requirements.in")
else:
    # A library uses a setup.py with requirements in it.
    os.remove("requirements.in")
    run("venv/bin/pip-compile setup.py")


run("venv/bin/pip-compile requirements-dev.in")
run("venv/bin/python -m pip install -r requirements-dev.txt")
run("git add .")
run("git commit -m Initial")
