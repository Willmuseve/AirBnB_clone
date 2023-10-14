#!usr/bin/python3

from models import *
from models.base_model import BaseModel


class User(BaseModel):
    """A class user that inherits from the base model
    and has email, password, first_name and last_name
    as public attributes"""

    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
