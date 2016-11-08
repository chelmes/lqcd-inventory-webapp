#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

from setuptools import setup, find_packages

setup(
    author="Martin Ueding",
    author_email="dev@martin-ueding.de",
    description="LQCD Inventory",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
    ],
    name="lqcd_inventory",
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    url="https://github.com/martin-ueding/lqcd-inventory-webapp",
    version="0.1",
)
