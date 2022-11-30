#!/usr/bin/python3
"""Unittest for review class: class and methods"""

import unittest
from models import review
from models.review import Review


class TestDocsReview(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(review.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
