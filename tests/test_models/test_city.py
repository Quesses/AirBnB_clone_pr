#!/usr/bin/python3
"""Unittest for city class: class and methods"""

import unittest
from models import city
from models.city import City


class TestDocsCity(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(city.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()