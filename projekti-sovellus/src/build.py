from src.initialize_database import initialize_database
from src.config import DATABASE_FILE_PATH

def build():
    initialize_database(DATABASE_FILE_PATH)

if __name__ == "__main__":
    build()
