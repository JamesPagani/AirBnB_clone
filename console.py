#!/usr/bin/env python3
# Author: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# console.py
"""This module contains the console application of the AirBnB web"""
import cmd
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is the console class"""
    prompt = '(hbnb) '

    def __init__(self):
        "Init method"
        super().__init__()
        self.__classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }
        self.__cmd = ""

    def do_EOF(self, line):
        'exit the program'
        print()
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
            instance = objects[key]
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
            for obj in storage.all().values():
                if class_name and obj.__class__.__name__ == class_name:
                    str_list.append(obj.__str__())
                elif not class_name:
                    str_list.append(obj.__str__())
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
        if "\"" in attr_v:
            attr_v = self.__quote_handler(attr_v)
        if not attr_v:
            return

        # Updating instance:
        forbbiden_attr = ["id", "created_at", "updated_at"]
        instance = objects[key]

        if attr_k not in forbbiden_attr:
            try:
                type_v = type(getattr(instance, attr_k))
                setattr(instance, attr_k, type_v(attr_v))
            except Exception:
                setattr(instance, attr_k, self.__data_converter(attr_v))
            finally:
                instance.save()
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

    def __quote_handler(self, attr):
        """
        This method parse the strings with quotes in order to
        use the update command without errors and recieving the
        quotes strings with spaces

        Args:
            attr (string): is the attribute_value where the parsing would
                            be saved
        Return:
            A (string) without quoutes.
            Also, it returns None if the string has no end quote and print
            the error
        """
        if ("\"" in attr[0]
                and "\"" in attr[len(attr) - 1]):
            return attr[1:-1]
        quote_list = []
        while attr:
            quote_list.append(attr)
            attr = self.__check_args(self.__cmd, None)
        if "\"" in quote_list[len(quote_list) - 1][-1:]:
            quote_str = quote_list[0][1:] + " "
            if (len(quote_list) > 2):
                quote_str += " ".join(quote_list[1:-1])
                quote_str += " "
            quote_str += quote_list[len(quote_list) - 1][:-1]
            return quote_str
        else:
            print("** value Error: No closing quotation **")
            return None

    def postloop(self):
        "do after the principal loop"
        print("", end="")

    def emptyline(self):
        "do nothign when press start"
        pass

    def precmd(self, line):
        "do before command"
        if line:
            self.__cmd = self.__parseline_generator(line)
            next(self.__cmd).split(".")
        return cmd.Cmd.precmd(self, line)

    def complete_create(self, text, line, begidx, endidx):
        "autocomplete classes"
        if not text:
            return list(self.__classes.keys())
        else:
            return [
                f for f in self.__classes.keys()
                if f.startswith(text)
                ]

    def complete_all(self, text, line, begidx, endidx):
        "autocomplete classes"
        if not text:
            return list(self.__classes.keys())
        else:
            return [
                f for f in self.__classes.keys()
                if f.startswith(text)
                ]

    def complete_destroy(self, text, line, begidx, endidx):
        "autocomplete classes"
        if not text:
            return list(self.__classes.keys())
        else:
            return [
                f for f in self.__classes.keys()
                if f.startswith(text)
                ]

    def complete_show(self, text, line, begidx, endidx):
        "autocomplete classes"
        if not text:
            return list(self.__classes.keys())
        else:
            return [
                f for f in self.__classes.keys()
                if f.startswith(text)
                ]

    def complete_update(self, text, line, begidx, endidx):
        "autocomplete classes"
        if not text:
            return list(self.__classes.keys())
        else:
            return [
                f for f in self.__classes.keys()
                if f.startswith(text)
                ]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
