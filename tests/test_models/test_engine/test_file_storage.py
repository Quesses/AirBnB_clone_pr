#!/usr/bin/python3
"""Unittest for FileStorage class: class and methods"""

import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestDocsFileStorage(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)

    def test_instance(self):
        """check if obj is an instance of BaseModel"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)


if __name__ == "__main__":
    unittest.main()