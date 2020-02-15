#!/usr/bin/env python3
# Author: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# console.py
"""This module contains the console application of the AirBnB web"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This is the console class"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        'exit the program'
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def postloop(self):
        print("", end="")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
