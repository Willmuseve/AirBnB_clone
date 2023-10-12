#!/usr/bin/python3
"""Base model class that defines all common attributes/methods."""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Base model class."""

    def __init__(self, *args, **kwargs):
        """Construct the class."""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                else:
                    continue
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return current instance's string representation(object)."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update updated_at field  with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the current instance's dictionary version."""
        class_name = self.__class__.__name__
        instance_dict = dict(self.__dict__)
        instance_dict['__class__'] = class_name
        instance_dict['updated_at'] = datetime.isoformat(self.updated_at)
        instance_dict['created_at'] = datetime.isoformat(self.created_at)
        return instance_dict
