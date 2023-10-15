#!/usr/bin/python3
"""FileStorage Module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes.
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    classes = {
            "BaseModel": BaseModel,
            "user": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path).
        Saves user object along with other objects
        """
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for key, obj_dict in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name in self.classes:
                        obj = self.classes[class_name](**obj_dict)
                        self.__objects[key] = obj
            except FileNotFoundError:
                pass


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
