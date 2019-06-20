from setuptools import setup


with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Programming Language :: Python :: {{ cookiecutter.python_version }}",
    ],
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=["{{ cookiecutter.project_slug }}"],
    test_suite="tests",
    version="{{ cookiecutter.project_version }}",
    license="Proprietary",
    zip_safe=False,
    extras_require={
        "dev": [
            "pytest==3.10.0",
            "pytest-cov==2.6.0",
            "pylint==2.1.1",
            "black==18.9b0",
            "bandit==1.5.1",
            "mypy==0.641",
            "tox==3.7.0",
        ]
    },
)
