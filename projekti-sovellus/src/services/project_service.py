from src.entities.project import Project, Music
from src.repositories.project_repository import project_repository as default_project_repository
from src.services.date_service import date_service

class ValidProjectError(Exception):
    pass

class ProjectService:
    """Projektien hallinnasta vastaava luokka, joka toimii sovelluksen logiikkakerroksessa."""

    def __init__(self, project_repository=default_project_repository):
        self._user = None
        self._project_repository = project_repository

    def create_project(self, name, description):
        """Luo uuden projektin ja tallentaa sen tietokantaan."""
        if not name:
            raise ValidProjectError("Project name cannot be empty")
        project = Project(name=name, description=description, user=self._user)
        return self._project_repository.create(project)

    def get_projects(self):
        """Hakee kaikki kirjautuneen käyttäjän projektit.
        Jos käyttäjä ei ole kirjautunut, hakee kaikki projektit"""
        if self._user:
            return self._project_repository.find_by_username(self._user.username)
        return self._project_repository.find_all()

    def get_projects_for_user(self, user):
        """Hakee kaikki käyttäjän projektit"""
        return self._project_repository.find_by_username(user.username)

    def delete_project(self, project):
        """Poistaa projektin tietokannasta."""
        self._project_repository.delete(project.id)

    def edit_project(self, project, new_name, new_description):
        """Muokkaa olemassa olevan projektin tietoja tietokannassa."""
        if not new_name:
            raise ValidProjectError("Project name cannot be empty")
        project.name = new_name
        project.description = new_description
        self._project_repository.update(project)

    def add_project_date(self, project, date_str, date_type):
        parsed_date = date_service(date_str)
        if not parsed_date:
            return False

        project.dates.append({
            "type": date_type,
            "date": parsed_date
        })
        self._project_repository.update(project)
        return True

    def delete_project_date(self, project, date_index):
        if date_index < 0 or date_index >= len(project.dates):
            return False

        project.dates.pop(date_index)
        self._project_repository.update(project)
        return True

    def add_project_music(self, project, title, file_path):
        music = Music(title=title, file_path=file_path)
        project.music_scores.append(music)
        self._project_repository.update(project)
        return music

    def delete_project_music(self, project, music):
        project.music_scores = [
            m for m in project.music_scores
            if not (m.title == music.title and m.file_path == music.file_path)
        ]
        self._project_repository.update(project)
        return True

project_service = ProjectService()
