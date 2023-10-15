#!usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """A class user that inherits from the base model
    and has email, password, first_name and last_name
    as public attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
