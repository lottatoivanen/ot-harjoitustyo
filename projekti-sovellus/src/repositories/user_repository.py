from src.entities.user import User
from src.database_connection import get_database_connection

def get_user_by_row(row):
    """Apufunktio, joka luo User-olion tietokantarivistä."""
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    """Käyttäjätietojen tallentamisesta ja hakemisesta vastaava luokka."""

    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        """Hakee kaikki käyttäjät tietokannasta."""
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM users"
        )
        rows = cursor.fetchall()
        return list(map(get_user_by_row, rows))

    def find_user_by_username(self, username):
        """Hakee käyttäjän käyttäjänimen perusteella."""
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT username, password FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()
        if row:
            return User(username=row[0], password=row[1])
        return None

    def create(self, user):
        """Luo uuden käyttäjän tietokantaan."""
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

user_repository = UserRepository(get_database_connection())
