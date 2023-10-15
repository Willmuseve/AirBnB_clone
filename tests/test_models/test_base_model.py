#!/usr/bin/python3
"""Tests for BaseModel."""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestCase Class for BaseModel."""

    def test_init(self):
        """Test all initial values and types."""
        base_mod = BaseModel()
        self.assertIsInstance(base_mod, BaseModel)
        self.assertIsInstance(base_mod.id, str)
        self.assertIsInstance(base_mod.created_at, datetime)
        self.assertIsInstance(base_mod.updated_at, datetime)

    def test_save(self):
        """Test save field."""
        base_mod = BaseModel()
        updated_at = base_mod.updated_at
        base_mod.save()
        base_mod.id = "azeaze"
        base_mod.save()
        self.assertNotEqual(base_mod.updated_at, updated_at)

    def test_to_dict2(self):
        """Test to_dict keys."""
        base_mod = BaseModel()
        base_keys_list = ['created_at', 'updated_at', '__class__', 'id']
        dict_value = base_mod.to_dict()
        for key in base_keys_list:
            self.assertIn(key, dict_value)

    def test_to_dict(self):
        """Test re-creation of from to_dict representation"""
        base_mod = BaseModel()
        base_mod_dict = base_mod.to_dict()
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
