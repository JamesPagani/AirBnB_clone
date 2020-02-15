#!/usr/bin/env python3
# Author: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# console.py
"""This module contains the console application of the AirBnB web"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This is the console class"""
    prompt = '(hbnb) '

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
        pass

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
        pass

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
