#!/bin/python3
"""State module."""
from models.base_model import BaseModel


class State(BaseModel):
    """Class state that inherits from the base model.

    and has public attribute name
    """

    name = ""
