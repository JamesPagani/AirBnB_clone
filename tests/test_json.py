#!/usr/bin/python3
# Author: Jaime Andrés Gálvez Villamarin
# tests/test_json.py
"""FileStorage unittest.
A test suite containing various tests for the FileStorage class and
its interaction with the BaseModel class.
"""

from datetime import datetime
from models.base_model import BaseModel
from models import storage
import unittest

class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage."""

    def test_FileStorage_attributes(self):
        """Checking if FileStorage attributes are correct."""
        self.assertEqual(type(storage._FileStorage__file_path), str,
                    msg="__file_path is either not private or not a string.")
        self.assertEqual(type(storage._FileStorage__objects), dir,
                    msg="__objects is either not private or not a dictionary.")

    def test_FileStorage_methods(self):
        """Checking if FileStorage methods exists."""
        try:
            storage.all
        except AttributeError:
            self.fail("storage.all is not public or does not exist at all.")
        try:
            storage.new
        except AttributeError:
            self.fail("")
        try:
            storage.save
        except AttributeError:
            self.fail("")
        try:
            storage.reload
        except AttributeError:
            self.fail("")

if __name__ == '__main__':
    unittest.main()
