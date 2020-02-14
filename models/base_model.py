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
        if kwargs:
            self.__dict__.update(kwargs)
            if "created_at" in self.__dict__:
                self.created_at = self.to_datetime(self.created_at)

            if "updated_at" in self.__dict__:
                self.updated_at = self.to_datetime(self.updated_at)
            if "__class__" in self.__dict__:
                del self.__dict__["__class__"]
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


    @staticmethod
    def to_datetime(iso_datetime):
        """From ISO string datetime to datetime.datetime."""
        list_datetime = iso_datetime.split(sep="T")
        list_datetime.extend(list_datetime.pop(0).split(sep="-"))
        list_datetime.extend(list_datetime.pop(0).split(sep=":"))
        list_datetime.extend(list_datetime.pop().split(sep="."))
        for i in range(len(list_datetime)):
            list_datetime[i] = int(list_datetime[i])
        return datetime(*list_datetime)
