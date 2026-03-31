import uuid

class Project:
    """Luokka projektia varten, jolla on nimi, kuvaus ja uniikki id."""
    def __init__(self, name, description, user, id=None):
        self.name = name
        self.description = description
        self.user = user
        self.id = id if id else str(uuid.uuid4())
