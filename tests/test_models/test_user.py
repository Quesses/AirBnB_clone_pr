#!/usr/bin/python3
"""Unittest for user Class: class and methods"""

import unittest
from models import user
from models.user import User


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()