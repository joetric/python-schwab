#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="python-schwab",
    version="0.1",
    description="Obtain transaction data from Schwab accounts.",
    author="Joseph Tricarico",
    author_email="jtricarico@gmail.com",
    url="http://github.com/joetric/python-schwab",
    license="MIT",
    long_description=read('README.md'),
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Programming Language :: Python :: 2.7',
    ],
    # dependency_links=[],
    install_requires=['BeautifulSoup', 'mechanize==0.2.5'], 
    test_suite='schwab.tests.tests',
)
