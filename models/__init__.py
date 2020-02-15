#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# /models/__init__.py
""" This module initialize the FileStorage engine"""
from file_storage import FileStorage

storage = FileStorage()
storage.reload()

if __name__ == '__main__':
    pass
