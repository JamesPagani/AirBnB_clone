#!/usr/bin/python3
"""Review class.
A review posted by an user for a lodging hosted in AirBnB.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """User review of a place."""

    place_id = ""
    user_id = ""
    text = ""
