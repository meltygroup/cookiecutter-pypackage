import os

if "{{ cookiecutter.type }}" == "application":
    os.remove("setup.py")
