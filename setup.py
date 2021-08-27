# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="stellaris-mod-janitor",
    version="0.1.0",
    description="A simple tool to help sanitize stellaris mods on linux",
    license="MIT",
    author="Andrew Burr",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['stellaris-janny=st_janny.cmd:main']
    },
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ]
)
