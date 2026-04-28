from src.entities.user import User
from src.repositories.user_repository import user_repository as default_user_repository

class InvalidCredentialsError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class UserService:
    """Käyttäjien hallinnasta vastaava luokka, joka toimii sovelluksen logiikkakerroksessa"""
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        """Tarkistaa kirjautumisessa käyttäjätiedot ja nostaa InvalidCredentialsError virhetilanteessa"""
        user = self._user_repository.find_user_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def get_current_user(self):
        """Hakee kirjautuneen käyttäjän."""
        return self._user

    def get_users(self):
        """Hakee kaikki käyttäjät."""
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tallentaa sen tietokantaan."""
        if self._user_repository.find_user_by_username(username):
            raise UsernameAlreadyExistsError(f"Username {username} already exists")

        user = User(username=username, password=password)
        self._user_repository.create(user)

        if login:
            self._user = user
        return user

user_service = UserService()
