# -*- coding: utf-8 -*-
""" Copyright (c) 2018"""
import codecs
import os

from setuptools import setup, find_packages

if os.path.exists('README.md'):
    long_description = codecs.open('README.md', 'r', 'utf-8').read()
else:
    long_description = 'See readme'

setup(
    name="Example",
    version="1.0",
    author="Alberto Vara",
    author_email="a.vara.1986@gmail.com",
    description="",
    long_description=long_description,
    classifiers=[
        'Development Status :: 4.0',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    license="MIT",
    platforms=["any"],
    keywords="kafka",
    url='',
    test_suite='nose.collector',
    packages=find_packages(),
    include_package_data=True,
)
