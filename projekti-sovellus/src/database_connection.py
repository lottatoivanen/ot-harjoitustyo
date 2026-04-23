import sqlite3
from config import DATABASE_FILE_PATH

_connection = None

def get_database_connection(database_path=DATABASE_FILE_PATH):
    global _connection

    if _connection is None:
        _connection = sqlite3.connect(database_path)
        _connection.row_factory = sqlite3.Row

    return _connection

def reset_database_connection():
    global _connection
    if _connection is not None:
        _connection.close()
    _connection = None
