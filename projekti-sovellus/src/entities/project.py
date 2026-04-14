import uuid

class Project:
    """Luokka projektia varten, jolla on nimi, kuvaus ja uniikki id."""
    def __init__(self, name, description, user, project_id=None):
        self.name = name
        self.description = description
        self.user = user
        self.id = project_id if project_id else str(uuid.uuid4())
