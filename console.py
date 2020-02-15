#!/usr/bin/env python3
# Author: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# console.py
"""This module contains the console application of the AirBnB web"""
import cmd
import sys
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """This is the console class"""
    prompt = '(hbnb) '

    def __init__(self):
        super().__init__()
        self.__classes = {
            'BaseModel': BaseModel
            }

    def do_EOF(self, line):
        'exit the program'
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id

        Args:
            <Class name>: desired instance of
        Usage:
            $ create <Class name>
            ex: $ create BaseModel
        """
        cmd = self.__parseline_generator(arg)
        try:
            className = next(cmd)
            if className in self.__classes:
                instance = self.__classes[className]()
                models.storage.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        except StopIteration:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id

        Args:
            <Class name> : class of the instance searched
            <id> : id of the instance searched
        Usage:
            $ show <Class name> <id>
            ex: $ show BaseModel 1234-1234-1234
        """
        cmd = self.__parseline_generator(arg)
        try:
            class_name = next(cmd)
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
        except StopIteration:
            print('** class name missing **')
            return

        try:
            id = next(cmd)
        except StopIteration:
            print('** instance id missing **')
            return

        objects = models.storage.all()
        key = "{}.{}".format(class_name, id)
        if key in objects:
            instance = self.__classes[class_name](objects[key])
            print(instance)
        else:
            print('** no instance found **')
            return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Args:
            <Class name> : class of the instance to delete
            <id> : id of the instance to delete
        Usage:
            $ destroy <Class name> <id>
            ex: $ destroy BaseModel 1234-1234-1234
        """
        pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Args:
            <Class name> (optional) : instances of to be printed
        Usage:
            $ all <Class name>
            ex: $ all BaseModel
            ---------or---------
            $ all
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Args:
            <Class name> : class of the instance to be modified
            <id> : id of the instance to be modified
            <attribute name> : name of the new attribute
            <attribute value> : value of the new attribute
        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
            ex: $ update BaseModel 1234-1234 email "aibnb@holbertonschool.com"

        Notes:
            *Only one attribute can be updated at the time
        """
        pass

    def postloop(self):
        print("", end="")

    def emptyline(self):
        pass

    def __parseline_generator(self, line):
        """It parse the commands but as a generator"""
        split = line.split()
        for i in split:
            yield i

    def __parseline(self, line):
        """It parse the commands an return as a list"""
        return line.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
