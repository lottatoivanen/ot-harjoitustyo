from src.database_connection import get_database_connection, reset_database_connection

def drop_tables(database_path = None):
    connection = get_database_connection(database_path)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS projects")
    connection.commit()

def create_tables(database_path = None):
    connection = get_database_connection(database_path)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            username TEXT,
            dates TEXT,
            FOREIGN KEY (username) REFERENCES users (username)
        )
    """)
    connection.commit()

def initialize_database(database_path = None):
    reset_database_connection()
    drop_tables(database_path)
    create_tables(database_path)

if __name__ == "__main__":
    initialize_database()
