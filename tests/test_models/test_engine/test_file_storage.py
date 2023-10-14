#!/usr/bin/python3
from unittest import TestCase, main
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_instance_storage(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        pass

    def test_save(self):
        pass

    def test_reload(self):
        pass


if __name__ == "__main__":
    main()
