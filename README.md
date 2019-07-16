# Cookiecutter PyPackage

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a
Python application or library.


## Using

To create a project using this template, simply run `cookiecutter`:

```bash
cookiecutter gh:meltygroup/cookiecutter-pypackage
```


## Handling requirements

Python projects should have broad dependencies to avoid
incompatibilities with other projects.

So a `setup.py` should look like:

```
install_requires=["aiohttp>=3.5.4,<4", "defusedxml>=0.5,<1"]
```

Or even this one if you feel maintaining it:

```
install_requires=["aiohttp", "defusedxml"]
```


## Deployments and test requirements

When you test an application or a library you may want the
dependencies to be a bit more pinned, and when you deploy an
application you want the dependencies to be clearly pinned.

To handle this, use a `requirements.txt` file with precisely pinned
dependencies, that your CI/CD can use. You can easily generate a
`requirements.txt` file by using:

```
pip-compile setup.py
```

from [pip-tools](https://pypi.org/p/pip-tools).
