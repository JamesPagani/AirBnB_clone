#!/usr/bin/env python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/engine/file_storage.py
"""This module contains the engine of persistence"""
from base_model import BaseModel
import json


class FileStorage():
    """FileStorage contains the engines to persist the data"""

    def __init__(self):
        self.__file_path = './file.json'
        self.__objects = dict()

    def all(self):
        """
        Returns the objects saved
        """
        return self.__objects

    def new(self, obj):
        """
        Set in in the __objects attribute the obj with key: <obj class name>.id
        """
        if obj:
            value = obj.to_dict()
            key = "{}.{}".format(value['__class'], value['id'])
            self.__objects[key] = value

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(self.__objects, file, ensure_ascii=False)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exist; otherwise, do nothing)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        except Exception:
            pass
