#!/usr/bin/python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="a1pamfax",
    version="0.0.1",
    author="Marc Bufe",
    author_email="bufemc@gmail.com",
    description="Python 3 implementation for the PamFax API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/bufemc/a1pamfax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='LICENSE.txt',
)
