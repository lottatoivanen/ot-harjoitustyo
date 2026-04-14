import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print("Varoitus: .env-tiedostoa ei löydy. Varmista, että se on luotu projektin juurikansioon.")

PROJECTS_FILENAME = os.getenv("PROJECT_FILENAME") or "projects.csv"
PROJECTS_FILE_PATH = os.path.join(dirname, "..", "data", PROJECTS_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
