#!/usr/bin/python3
""" Unittest module for the class BaseModel and its methods"""

import Unittest
import os
import models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    """Test for class BaseModel outputs"""

    def test_unique_id(self):
        """test that every id is unique to each instance"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1, inst2)

    def test_id_type(self):
        """Test for the correct type of id"""
        inst1 = BaseModel()
        selfassertEqual("<class 'str'>", str(type(inst1.id)))

    def test_save(self):
        """
        Test for each time an instance is saved, the
        update_at attribute is updated accordingly
        """
        inst1 = BaseModel()
        update_at_attr_before_save = inst1.update_at
        inst1.save()
        update_at_attr_after_save = inst1.update_at
        self.assertNotEqual(update_at_attr_before_save, update_at_attr_after_save)

    def test_file_exec(self):
        """Test if file has reaad, write and execute permision"""
        read = os.access('models/base_model.py', os.R_OK)
        self.assertEqual(True, read)
        write = os.access("models/base_model.py", os.W_OK)
        self.assertEqual(True, write)
        exec = os.access('models/base_model.py', os.X_OK)
        self.assertEqual(True, exec)

    def test_to_dict(self):
        """
        test_to_dict method that test if a dictionary is returned
        and if updated_at and created_at attributes are in the correct
        format
        """
        instance1 = BaseModel()
        instance1_User = User()
        # test type of return
        self.assertEqual('<class \'dict\'>', str(type(instance1.to_dict())))

        updated_expected_format = instance1.updated_at.isoformat()
        created_expected_format = instance1.created_at.isoformat()
        class_attr_value_expected = type(instance1_User).__name__
        updated_actual_format = instance1.to_dict()["updated_at"]
        created_actual_format = instance1.to_dict()["created_at"]
        class_attr_value_get = instance1_User.to_dict()['__class__']
        # test format inside the dictionary
        self.assertEqual(updated_expected_format, updated_actual_format)
        self.assertEqual(created_expected_format, created_actual_format)
        self.assertEqual(class_attr_value_expected, class_attr_value_get)

if __name__ == "__main__":
    unittest.main()