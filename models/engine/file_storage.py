#!/usr/bin/env python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/engine/file_storage.py
"""This module contains the engine of persistence"""
import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage contains the engines to persist the data"""

    def __init__(self):
        """
        Init method of thf FileStorage
        """
        self.__file_path = 'file.json'
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
            key = "{}.{}".format(value['__class__'], value['id'])
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

    def list_by_class(self, class_name, class_var):
        """
        this method do a search for all keys that contains the given class_name

        Args:
            class_name (str):Is the name of the instances' class to be searched
            class_var (Class): Is the class, is used to instance a copy
        Return:
            list (list) of the __str__ representation of the founded instances
            It is an empty list if it did not found instances of the given
            class_name
        """
        return_list = []
        for k in self.__objects:
            if class_name in k:
                instance = class_var(**self.__objects[k]).__str__()
                return_list.append(instance)
        return return_list
