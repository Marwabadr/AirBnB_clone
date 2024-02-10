#!/usr/bin/python3
"""
Test module for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_attributes(self):
        """Test initialization of attributes"""
        mod = BaseModel()
        self.assertTrue(hasattr(mod, 'id'))
        self.assertTrue(hasattr(mod, 'created_at'))
        self.assertTrue(hasattr(mod, 'updated_at'))

    def test_str_representation(self):
        """Test __str__ method"""
        mod = BaseModel()
        str_repr = str(mod)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(str(mod.id), str_repr)
        self.assertIn(str(mod.__dict__), str_repr)

    def test_save_method(self):
        """Test save method"""
        mod = BaseModel()
        old_updated_at = mod.updated_at
        mod.save()
        self.assertNotEqual(old_updated_at, mod.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        mod = BaseModel()
        mod_dict = mod.to_dict()
        self.assertIsInstance(mod_dict, dict)
        self.assertEqual(mod_dict['__class__'], 'BaseModel')
        self.assertEqual(mod_dict['created_at'], mod.created_at.isoformat())
        self.assertEqual(mod_dict['updated_at'],  mod.updated_at.isoformat())
