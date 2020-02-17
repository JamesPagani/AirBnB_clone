#!/usr/bin/python3
"""User class.
A representation of an AirBnB user."""


from models.base_model import BaseModel


class User(BaseModel):
    """AirBnB user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
