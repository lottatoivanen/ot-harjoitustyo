from entities.project import Project

class ProjectService:
    """Projektien hallinnasta vastaava luokka, joka toimii sovelluksen logiikkakerroksessa."""
    def __init__(self):
        self._projects = []

    def create_project(self, name, description, user):
        """Luo uuden projektin ja lisää sen projektien listaan."""
        project = Project(name, description, user)
        self._projects.append(project)
        return project

    def get_all_projects(self):
        """Palauttaa listan kaikista projekteista."""
        return self._projects