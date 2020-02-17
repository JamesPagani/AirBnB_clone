#!/usr/bin/python3
"""City class.
A state city where an available lodging hosted on AirBnB is.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """A City where an available lodging is."""

    state_id = ""
    name = ""
