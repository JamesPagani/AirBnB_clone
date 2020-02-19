#!/usr/bin/python3
"""State class.
A State in the world where available lodgings are hosted in AirBnB.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """A State in the world."""

    name = ""
