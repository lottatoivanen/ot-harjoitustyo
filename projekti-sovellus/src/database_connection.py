import sqlite3
from src.config import DATABASE_FILE_PATH

_CONNECTION = None

def get_database_connection(database_path=DATABASE_FILE_PATH):
    """Yhdistää tietokannan sovellukseen"""
    global _CONNECTION

    if _CONNECTION is None:
        _CONNECTION = sqlite3.connect(database_path)
        _CONNECTION.row_factory = sqlite3.Row

    return _CONNECTION

def reset_database_connection():
    """Resetoi tietokantayhteyden"""
    global _CONNECTION
    if _CONNECTION is not None:
        _CONNECTION.close()
    _CONNECTION = None
