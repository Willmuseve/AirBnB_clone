#!/usr/bin/python3
"""Base model class tthat defines all common attributes/methods."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base model class."""

    def __init__(self):
        """Construct the class."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return current instance's string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at field  with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the current instance's dictionary version."""
        instance_dict = dict(self.__dict__)
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['updated_at'] = datetime.isoformat(self.updated_at)
        instance_dict['created_at'] = datetime.isoformat(self.created_at)
        return instance_dict
