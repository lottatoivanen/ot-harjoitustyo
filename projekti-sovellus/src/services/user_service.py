from entities.user import User
from repositories.user_repository import user_repository as default_user_repository

class InvalidCredentialsError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class UserService:
    """Käyttäjien hallinnasta vastaava luokka, joka toimii sovelluksen logiikkakerroksessa"""

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = default_user_repository
    
    def login(self, username, password):
        user = self._user_repository.find_user_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        
        self._user = user
        return user

    def get_current_user(self):
        return self._user
    
    def get_users(self):
        return self._user_repository.find_all()
    
    def logout(self):
        self._user = None
    
    def create_user(self, username, password, login=True):
        if self._user_repository.find_user_by_username(username):
            raise UsernameAlreadyExistsError(f"Username {username} already exists")
        
        user = User(username=username, password=password)
        self._user_repository.create(user)

        if login:
            self._user = user
        return user

user_service = UserService()
