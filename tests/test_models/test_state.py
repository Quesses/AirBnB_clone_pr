#!/usr/bin/python3
"""Unittest for state class: class and methods"""

import unittest
from models import state
from models.state import State


class TestDocsState(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(state.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
