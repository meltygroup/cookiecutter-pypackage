# Cookiecutter PyPackage

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a
Python application or library.


## Using

To create a project using this template, simply run `cookiecutter`:

```bash
cookiecutter gh:meltygroup/cookiecutter-pypackage
```


## Differences between application and library

This cookiecutter asks if you're building a library or an application,
both will create a single Python package, with a module in it, so
here's the key differences:

### Application

A Python application should have precise (pinned) dependencies, we're
achieving this thrue a `requirements.txt`.


### Library

A Python library should have broad dependencies to avoid
incompatibilities with other libraries used in a same application,
we're achieving this thrue a `setup.py`.
