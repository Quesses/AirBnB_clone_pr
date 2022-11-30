#!/usr/bin/python3
"""Unittest for place class: class and methods"""

import unittest
from models import place
from models.place import Place


class TestDocsplace(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(place.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
