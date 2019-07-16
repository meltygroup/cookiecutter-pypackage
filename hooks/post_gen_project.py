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
run("git add .")
run("git commit -m Initial")
