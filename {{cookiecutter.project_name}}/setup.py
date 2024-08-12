#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

setup(
    name='{{cookiecutter.project_slug}}',
    packages=find_packages(
        include=['{{cookiecutter.project_slug}}', '{{cookiecutter.project_slug}}.*']
    ),
    test_suite='tests',
    version="{{cookiecutter.version}}",
)
