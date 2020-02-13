#!/usr/bin/python3
"""Base Model.
Main template for all other classes inside this project.
"""


from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Template for all other classes."""

    def __init__(self):
        """Initialize a new class object."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,\
                                     self.__dict__)

    def save(self):
        """Update 'updated_at' attribute."""
        self.created_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
