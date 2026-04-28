from src.entities.project import Project
from src.repositories.user_repository import user_repository
from src.database_connection import get_database_connection

def get_project_by_row(row):
    """Apufunktio, joka luo Project-olion tietokantarivistä."""
    if row:
        project_id = row[0]
        name = row[1]
        description = row[2]
        username = row[3]
        dates = row[4]
        user = user_repository.find_user_by_username(username) if username else None
        return Project(
            project_id=project_id,
            name=name,
            description=description,
            user=user,
            dates=Project.dates_from_json(dates),
        )
    return None

class ProjectRepository:
    """Vastaa projektien tietokantaoperaatioista."""

    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        """Hakee kaikki projektit tietokannasta."""
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, name, description, username, dates FROM projects"
        )
        rows = cursor.fetchall()
        projects = []
        for row in rows:
            project = get_project_by_row(row)
            if project:
                projects.append(project)
        return projects

    def find_by_username(self, username):
        """Hakee projektit käyttäjän nimen perusteella."""
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, name, description, username, dates FROM projects WHERE username = ?",
            (username,)
        )
        rows = cursor.fetchall()
        projects = []
        for row in rows:
            project = get_project_by_row(row)
            if project:
                projects.append(project)
        return projects

    def create(self, project):
        """Luo uuden projektin tietokantaan."""
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO projects (name, description, username, dates) VALUES (?, ?, ?, ?)",
            (
                project.name,
                project.description,
                project.user.username if project.user else None,
                project.dates_to_json(),
            )
        )
        self._connection.commit()
        project.id = cursor.lastrowid
        return project

    def delete(self, project_id):
        """Poistaa projektin tietokannasta."""
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM projects WHERE id = ?",
            (project_id,)
        )
        self._connection.commit()

    def update(self, project):
        """Päivittää projektin tietokannassa."""
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE projects SET name = ?, description = ?, dates = ? WHERE id = ?",
            (project.name, project.description, project.dates_to_json(), project.id)
        )
        self._connection.commit()

project_repository = ProjectRepository(get_database_connection())
