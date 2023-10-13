#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
        JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        Saves user object along with other objects
        """
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    objects_dict = json.load(file)
                    for key, obj_dict in objects_dict.items():
                        if '__class__' in obj_dict and obj_dict['__class__'] =\
                                = "User":
                            obj = User(**obj_id)
                        else:
                            class_name, obj_id = key.split('.')
                            obj = eval(class_name)(**obj_dict)
                            self.__objects[key] = obj
            except FileNotFoundError:
                pass


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
