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

        try:
            dictionary = model.to_dict()
        except AttributeError:
            self.fail("to_dict method is not implemented")
        self.assertEquals(dictionary['__class__'], "BaseModel")

    def test_create_BaseModel_from_dictionary(self):
        model = BaseModel()
        dictionary = model.to_dict()

        try:
            model_copy = BaseModel(**dictionary)
        except TypeError:
            self.fail("Arguments are not implemented")

        self.assertEqual(model.id, model_copy.id)
        self.assertEqual(model.created_at, model_copy.created_at)
        self.assertEqual(model.updated_at, model_copy.updated_at)
        self.assertIsNot(model, model_copy)

        model.save()
        dictionary = model.to_dict()

        self.assertEqual(model.id, model_copy.id)
        self.assertEqual(model.created_at, model_copy.created_at)
        self.assertIsNotEqual(model.updated_at, model_copy.updated_at)
        self.assertIsNot(model, model_copy)

        model_copy = BaseModel(**dictionary)

        self.assertEqual(model.id, model_copy.id)
        self.assertEqual(model.created_at, model_copy.created_at)
        self.assertEqual(model.updated_at, model_copy.updated_at)
        self.assertIsNot(model, model_copy)

        dictionary['name'] = 'Jaime'
        dictionary['age'] = 21
        dictionary['gender'] = 'male videogamer'
        dictionary['strength'] = 121.5

        model_copy = BaseModel(**dictionary)
        try:
            name = model_copy.name
            age = model_copy.age
            gender = model_copy.gender
            strength = model_copy.strength
        except AttributeError as err:
            self.fail(err.args)

        self.assertEqual(name, dictionary['name'])
        self.assertEqual(age, dictionary['age'])
        self.assertEqual(gender, dictionary['gender'])
        self.assertEqual(strength, dictionary['strength'])


if __name__ == '__main__':
    unittest.main()
