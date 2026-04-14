from pathlib import Path
from entities.project import Project
from repositories.user_repository import user_repository
from config import PROJECTS_FILE_PATH

class ProjectRepository:
    """Vastaa projektien tietokantaoperaatioista."""

    def __init__(self):
        self._file_path = PROJECTS_FILE_PATH

    def find_all(self):
        return self._read()

    def find_by_username(self, username):
        projects = self._read()
        user_projects = filter(lambda p: p.user and p.user.username == username, projects)
        return list(user_projects)

    def create(self, project):
        projects = self._read()
        projects.append(project)
        self._write(projects)
        return project

    def delete(self, project_id):
        projects = self._read()
        projects_without_id = filter(lambda p: p.id != project_id, projects)
        self._write(projects_without_id)

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        projects = []
        self._ensure_file_exists()
        with open(self._file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.replace("\n", "")
                parts = line.split(";")
                project_id = parts[0]
                name = parts[1]
                description = parts[2]
                username = parts[3]
                user = user_repository.find_user_by_username(username) if username else None
                projects.append(
                    Project(project_id=project_id, name=name, description=description, user=user)
                    )
        return projects

    def _write(self, projects):
        self._ensure_file_exists()
        with open(self._file_path, "w", encoding="utf-8") as file:
            for project in projects:
                user_part = project.user.username if project.user else ""
                line = f"{project.id};{project.name};{project.description};{user_part}\n"
                file.write(line)

project_repository = ProjectRepository()
