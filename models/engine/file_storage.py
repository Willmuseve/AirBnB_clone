#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel

class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
        JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {}
        for key, obj in FileStorage.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                    objects_dict = json.load(file)
                    for key, obj_dict in objects_dict.items():
                        class_name, obj_id = key.split('.')
                        obj = eval(class_name)(**obj_dict)
                        FileStorage.__objects[key] = obj
            except FileNotFoundError:
                pass


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
