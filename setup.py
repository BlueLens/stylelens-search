# coding: utf-8

"""
    stylelens-search

    This is a API document for Image search on fashion items\"

    OpenAPI spec version: 0.0.1
    Contact: devops@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "stylelens-search"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="stylelens-search",
    author_email="devops@bluehack.net",
    url="",
    keywords=["Swagger", "stylelens-search"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is a API document for Image search on fashion items\&quot;
    """
)
