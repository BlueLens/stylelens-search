# coding: utf-8

"""
    stylelens-search

    This is a API document for Image search on fashion items\"

    OpenAPI spec version: 0.0.1
    Contact: devops@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import stylelens_search
from stylelens_search.rest import ApiException
from stylelens_search.apis.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """ SearchApi unit test stubs """

    def setUp(self):
        self.api = stylelens_search.apis.search_api.SearchApi()

    def tearDown(self):
        pass

    def test_search_image(self):
        """
        Test case for search_image

        Query to search images
        """
        pass


if __name__ == '__main__':
    unittest.main()