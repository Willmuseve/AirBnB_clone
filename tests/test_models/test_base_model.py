#!/usr/bin/python3
import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_mod = BaseModel()

    def test_initial_values_types(self):
        self.assertIsInstance(self.base_mod, BaseModel)
        self.assertIsInstance(self.base_mod.id, str)
        self.assertIsInstance(self.base_mod.created_at, datetime.datetime)
        self.assertIsInstance(self.base_mod.updated_at, datetime.datetime)

    def test_if_updated_at_get_updated_after_calling_save(self):
        prev_updated_at = self.base_mod.updated_at
        self.base_mod.save()
        self.assertNotEqual(self.base_mod.updated_at, prev_updated_at)

    def test_to_dict_return_type(self):
        self.assertIsInstance(self.base_mod.to_dict(), dict)

    def test_dict_keys_from_to_dict(self):
        base_keys_list = ['created_at', 'updated_at', '__class__', 'id']
        dict_value = self.base_mod.to_dict()
        for key in base_keys_list:
            self.assertIn(key, dict_value)

    def test_re_creation_from_dict_representation(self):
        re_created = BaseModel(self.base_mod.to_dict())
        self.assertIsInstance(re_created, BaseModel)
        keys_list = list(self.base_mod.to_dict())
        for key in keys_list:
            self.assertEqual(
                    getattr(re_created, key),
                    getattr(self.base_mod, key)
                    )


if __name__ == "__main__":
    unittest.main()
