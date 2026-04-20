from entities.project import Project
from repositories.project_repository import project_repository as default_project_repository

class ProjectService:
    """Projektien hallinnasta vastaava luokka, joka toimii sovelluksen logiikkakerroksessa."""

    def __init__(self, project_repository=default_project_repository):
        self._user = None
        self._project_repository = project_repository

    def create_project(self, name, description):
        project = Project(name=name, description=description, user=self._user)
        return self._project_repository.create(project)

    def get_projects(self):
        if self._user:
            return self._project_repository.find_by_username(self._user.username)
        return self._project_repository.find_all()

    def get_projects_for_user(self, user):
        return self._project_repository.find_by_username(user.username)

project_service = ProjectService()