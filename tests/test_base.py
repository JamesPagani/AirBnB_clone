#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# test/test_base.py
"""This module contains test cases for a Base class"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    @classmethod
    def setUpClass(self):
        print("[Start of Base Test cases]")

    @classmethod
    def tearDownClass(self):
        print("Done")

    def test_public_attributes(self):
        """Checouts that the attributes are public"""
        model = BaseModel()
        try:
            id = model.id
        except AttributeError:
            self.fail("id attribute is not public or implemented")
        try:
            created_at = model.created_at
        except AttributeError:
            self.fail("created_at attribute is not public or implemented")
        try:
            updated_at = model.updated_at
        except AttributeError:
            self.fail("updated_at attribute is not public or implemented")

    def test_datatype(self):
        """Checouts attributes data type"""
        model = BaseModel()
        self.assertIsInstance(
            model.id,
            str,
            "Id is not an intance of str")
        self.assertIsInstance(
            model.created_at,
            datetime.datetime,
            "created_at is not an intance of datetime")
        self.assertIsInstance(
            model.updated_at,
            datetime.datetime,
            "updated_at is not an intance of datetime")

    def test_str_function(self):
        model = BaseModel()
        test = "[BaseModel] ({:s}) ({})".format(model.id, model.__dict__)
        self.assertEqual(
            test,
            model.__str__(),
            "BasSeModel.__str__: {:s}, \nMUST BE:\n{:s}".format(
                model.__str__(),
                test
                )
        )

    def test_save_function(self):
        model = BaseModel()
        created = model.created_at
        updated = model.updated_at
        try:
            model.save()
        except AttributeError:
            self.fail("BaseModel has not implemented the save function")
        else:
            self.assertEqual(
                created.minute,
                model.created_at.minute,
                "expected Created: {}, current: {}".format(
                    created,
                    model.created_at
                    )
                )
            self.assertNotEqual(
                updated,
                model.created_at,
                "expected updated: {}, current: {}".format(
                    updated.minute,
                    model.updated_at.minute
                    )
                )

    def test_to_dict_function(self):
        model = BaseModel()
        created = model.created_at
        updated = model.updated_at

        try:
            dictionary = model.to_dict()
        except AttributeError:
            self.fail("to_dict method is not implemented")

        test_created = "{:d}-{:d}-{:d}T{:d}:{:d}.{:f}".format(
            created.year,
            created.month,
            created.day,
            created.hour,
            created.minute,
            created.second,
            created.microsecond
        )
        test_updated = "{:d}-{:d}-{:d}T{:d}:{:d}.{:f}".format(
            updated.year,
            updated.month,
            updated.day,
            updated.hour,
            updated.minute,
            updated.second,
            updated.microsecond
        )

        self.assertEqual(
            dictionary['created_at'],
            test_created,
        )
        self.assertEqual(
            dictionary['updated_at'],
            test_updated,
        )
        self.assertEquals(dictionary['__class__'], "BaseModel")


if __name__ == '__main__':
    unittest.main()
