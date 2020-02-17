#!/usr/bin/python3
# Author: Jaime Gálvez(JamesPagani) <ur email bruh>
# Collaborator: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# models/base_model.py
"""Base Model.
Main template for all other classes inside this project.
"""


from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Template for all other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new class object."""
        if kwargs:
            self.__dict__.update(kwargs)
            if "created_at" in self.__dict__:
                self.created_at = datetime.strptime(self.created_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")

            if "updated_at" in self.__dict__:
                self.updated_at = datetime.strptime(self.updated_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            if "__class__" in self.__dict__:
                del self.__dict__["__class__"]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update 'updated_at' attribute."""
        self.created_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
