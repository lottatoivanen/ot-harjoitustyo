from database_connection import get_database_connection

def drop_tables():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS projects")
    connection.commit()

def create_tables():
    connection = get_database_connection()
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
            FOREIGN KEY (username) REFERENCES users (username)
        )
    """)
    connection.commit()

def initialize_database():
    drop_tables()
    create_tables()

if __name__ == "__main__":
    initialize_database()
