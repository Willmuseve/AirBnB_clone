#!/usr/bin/python3
"""Review module."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Revies which inherits from the base modes with the.

    following public attributes:
    """

    place_id = ""  # It will be the Place.id
    user_id = ""  # It will be the User.id
    text = ""
