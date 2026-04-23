from initialize_database import initialize_database

def build():
    initialize_database("database.sqlite")

if __name__ == "__main__":
    build()
