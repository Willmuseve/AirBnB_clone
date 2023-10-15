#!usr/bin/python3
"""Amenity module."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class amenity that inherits from the basemodel.

    and has public attribute name
    """

    name = ""
