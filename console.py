#!/usr/bin/env python3
# Author: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# console.py
"""This module contains the console application of the AirBnB web"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is the console class"""
    prompt = '(hbnb) '

    def __init__(self):
        super().__init__()
        self.__classes = {
            'BaseModel': BaseModel
            }
        self.__cmd = ""

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
        className = self.__check_args(
            self.__cmd,
            "** class name missing **")

        if not className:
            pass
        elif className in self.__classes:
            instance = self.__classes[className]()
            storage.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

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
        # Handle class_name argument:
        class_name = self.__check_args(self.__cmd, "** class name missing **")
        if not class_name:
            return
        if class_name and class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        # Handel id argument:
        id = self.__check_args(self.__cmd, "** instance id missing **")
        if not id:
            return

        # Print instances
        objects = storage.all()
        key = "{}.{}".format(class_name, id)
        if key in objects:
            instance = self.__classes[class_name](**objects[key])
            print(instance)
        else:
            print('** no instance found **')

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
        # Handle class_name argument:
        class_name = self.__check_args(self.__cmd, "** class name missing **")
        if not class_name:
            return
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        # Handle id argument:
        id = self.__check_args(self.__cmd, "** instance id missing **")
        if not id:
            return

        # Destroy object
        objects = storage.all()
        key = "{}.{}".format(class_name, id)
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print('** no instance found **')

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
        # Handle class_name argument:
        class_name = self.__check_args(self.__cmd, None)
        if class_name and class_name not in self.__classes:
            print("** class doesn't exist **")
        else:
            str_list = []
            for dictionary in storage.all().values():
                class_v = self.__classes[dictionary['__class__']]
                instance = class_v(**dictionary)
                if class_name and instance.__class__.__name__ == class_name:
                    str_list.append(instance.__str__())
                elif not class_name:
                    str_list.append(instance.__str__())
            print(str_list)

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
        # Handle class_name argument:
        class_name = self.__check_args(self.__cmd, "** class name missing **")
        if not class_name:
            return
        elif class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        # Handle id argument:
        id = self.__check_args(self.__cmd, "** instance id missing **")
        if not id:
            return

        # Handle <class_name>.<id> key existence:
        key = "{}.{}".format(class_name, id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        # Handle attr_k argument:
        attr_k = self.__check_args(self.__cmd, "** attribute name missing **")
        if not attr_k:
            return

        # Handle attr_v argument:
        attr_v = self.__check_args(self.__cmd, "** value missing **")
        if not attr_v:
            return

        # Updating instance:
        forbbiden_attr = ["id", "created_at", "updated_at"]
        dictionary = objects[key]

        if attr_k not in forbbiden_attr:
            try:
                type_v = type(dictionary[attr_k])
                dictionary[attr_k] = type_v(attr_v)
            except Exception:
                dictionary[attr_k] = attr_v

            instance = self.__classes[class_name](**dictionary)
            storage.new(instance)
            storage.save()

    def __parseline_generator(self, line):
        """
        It parse the commands but as a generator that's mean that
        you need to use the next() to get the next value of the list.
        Also, you know that the generator has no more elements when the
        StopIterator exception is raised.

        Args:
            line (string): given line of the command with the args
        Return
            args (generator) splited by black spaces
        """
        split = line.split()
        for i in split:
            yield i

    def __data_converter(self, value):
        """
        This method tries to convert a given value to an
        int or float

        Args:
            value (string): string value could contains a number
        Return:
            value variable as an (int), (float) or (string) if the previous
            convertions fails
        """
        # try to convert to int:
        try:
            return int(value)
        except Exception:
            pass
        # try to convert to float:
        try:
            return float(value)
        except Exception:
            pass
        return str(value)

    def __check_args(self, cmd, err_message=""):
        """
        This method checkout if it is posible to get an argument
        of the given cmd generator list

        Args:
            cmd (generator): Is a generator list with the arguments
            err_message (str): Is the error message in case that there
                                were a problem getting the next argument
        Return:
            argument (str) if it was possible to get an argument of the cmd
            None if it wasn't possible
        """
        try:
            return next(cmd)
        except StopIteration:
            if err_message:
                print(err_message)
            return None

    def postloop(self):
        print("", end="")

    def emptyline(self):
        pass

    def precmd(self, line):
        if line:
            self.__cmd = self.__parseline_generator(line)
            next(self.__cmd)
        return cmd.Cmd.precmd(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
