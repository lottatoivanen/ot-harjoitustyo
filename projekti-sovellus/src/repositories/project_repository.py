from pathlib import Path
from entities.project import Project
from repositories.user_repository import user_repository
from database_connection import get_database_connection

def get_project_by_row(row):
    if row:
        project_id = row[0]
        name = row[1]
        description = row[2]
        username = row[3]
        user = user_repository.find_user_by_username(username) if username else None
        return Project(project_id=project_id, name=name, description=description, user=user)
    return None

class ProjectRepository:
    """Vastaa projektien tietokantaoperaatioista."""

    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, name, description, username FROM projects"
        )
        rows = cursor.fetchall()
        projects = []
        for row in rows:
            project = get_project_by_row(row)
            if project:
                projects.append(project)
        return projects

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, name, description, username FROM projects WHERE username = ?",
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
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO projects (name, description, username) VALUES (?, ?, ?)",
            (project.name, project.description, project.user.username if project.user else None)
        )
        self._connection.commit()
        return project

    def delete(self, project_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM projects WHERE id = ?",
            (project_id,)
        )
        self._connection.commit()

project_repository = ProjectRepository(get_database_connection())
