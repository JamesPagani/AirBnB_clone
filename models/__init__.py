#!/usr/bin/python3
# Author: Jhonatan Arenas (Cybernuki) <1164@holbertonschool.com>
# /models/__init__.py
""" This module initialize the FileStorage engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
