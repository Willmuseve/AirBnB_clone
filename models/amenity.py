#!usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class amenity that inherits from the basemodel
    and has public attribute name"""

    name = ""
