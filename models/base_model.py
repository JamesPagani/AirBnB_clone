#!/usr/bin/python3
"""Base Model.
Main template for all other classes inside this project.
"""


from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Template for all other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new class object."""
        if kwargs is not None:
            self.__dict__.update(kwargs)
            if "created_at" in self.__dict__:
                self.created_at = self.created_at.split(sep="T")
                self.created_at.extend(self.created_at.pop(0).split(sep="-"))
                self.created_at.extend(self.created_at.pop(0).split(sep=":"))
                self.created_at.extend(self.created_at.pop().split(sep="."))
                for i in range(len(self.created_at)):
                    self.created_at[i] = int(self.created_at[i])
                self.created_at = datetime(*self.created_at)

            if "updated_at" in self.__dict__:
                self.updated_at = self.updated_at.split(sep="T")
                self.updated_at.extend(self.created_at.pop(0).split(sep="-"))
                self.updated_at.extend(self.created_at.pop(0).split(sep=":"))
                self.updated_at.extend(self.created_at.pop().split(sep="."))
                for i in range(len(self.updated_at)):
                    self.updated_at[i] = int(self.updated_at)
                self.updated_at = datetime(*self.updated_at)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
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
