class User:
    """Luokka käyttäjälle, jolla on käyttäjätunnus ja salasana."""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.projects = []
