#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """Class city that inherits from the basemodel
    and has public attributes state_id and name """

    state_id = ""
    name = ""
