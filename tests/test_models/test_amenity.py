#!/usr/bin/python3
"""Unittest for amenity class: class and methods"""

import unittest
from models import amenity
from models.amenity import Amenity


class TestDocsAmenity(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()