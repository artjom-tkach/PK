import os
import sqlite3

from .select import Select
from .delete import Delete
from .insert import Insert
from .update import Update


class Sqlite3(Select, Insert, Update, Delete):
    connection = None
    __database_file = f'{os.path.dirname(os.path.abspath(__file__))}/sqlite.db'

    def __init__(self):
        self.connect()
        super().__init__(self)

    def __del__(self):
        self.close_connection()

    def connect(self):
        if self.is_connected():
            return True

        try:
            self.connection = sqlite3.connect(self.__database_file)
            return True
        except Exception as e:
            print(e)

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                print(e)

    def is_connected(self):
        if self.connection:
            try:
                self.connection.cursor()
                return True
            except Exception:
                return False

        return False
