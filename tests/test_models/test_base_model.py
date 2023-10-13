#!/usr/bin/python3
"""Tests for BaseModel."""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestCase Class for BaseModel."""

    def setUp(self):
        """Set things up for tests."""
        self.base_mod = BaseModel()

    def test_initial_values_types(self):
        """Test all initial values and types."""
        self.assertIsInstance(self.base_mod, BaseModel)
        self.assertIsInstance(self.base_mod.id, str)
        self.assertIsInstance(self.base_mod.created_at, datetime)
        self.assertIsInstance(self.base_mod.updated_at, datetime)

    def test_if_updated_at_get_updated_after_calling_save(self):
        """Test updated_at field."""
        prev_updated_at = self.base_mod.updated_at
        self.base_mod.save()
        self.assertNotEqual(self.base_mod.updated_at, prev_updated_at)

    def test_to_dict_return_type(self):
        """Test dict return."""
        self.assertIsInstance(self.base_mod.to_dict(), dict)

    def test_dict_keys_from_to_dict(self):
        """Test to_dict keys."""
        base_keys_list = ['created_at', 'updated_at', '__class__', 'id']
        dict_value = self.base_mod.to_dict()
        for key in base_keys_list:
            self.assertIn(key, dict_value)

    def test_re_creation_from_dict_representation(self):
        """Test re-creation of from to_dict representation"""
        base_mod_dict = self.base_mod.to_dict()
        re_created = BaseModel(**base_mod_dict)
        self.assertIsInstance(re_created, BaseModel)
        if re_created.__class__ == base_mod_dict["__class__"]:
            raise AttributeError("__class__ from kwargs is an attribute")
        for key in base_mod_dict.keys():
            if key in ["created_at", "updated_at"]:
                self.assertEqual(
                        datetime.isoformat(getattr(re_created, key)),
                        base_mod_dict[key]
                )
            else:
                if key != "__class__":
                    self.assertEqual(
                            getattr(re_created, key),
                            base_mod_dict[key]
                    )


if __name__ == "__main__":
    unittest.main()
