from src.ui.main_view import MainView
from src.ui.login_view import LoginView
from src.ui.register_view import RegisterView
from src.services.project_service import project_service
from src.services.user_service import user_service

class UI:
    """Sovelluksen pääkäyttöliittymä, joka sisältää projektien listausnäkymän sekä kirjautumis- ja rekisteröitymisnäkymän"""
    def __init__(self, root):
        self._root = root
        self._projects = []
        self._current_view = None

    def start(self):
        """Näyttää käyttöliittymän aloitusnäkymän eli kirjautumisnäkymän"""
        self.show_login_view()

    def clear_view(self):
        """Tuhoaa nykyisen näkymän, jos sellainen on."""
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None

    def show_projects_view(self):
        """Näyttää projektien listausnäkymän kirjautuneelle käyttäjälle."""
        self.clear_view()
        project_service._user = user_service.get_current_user()
        self._projects = project_service.get_projects()
        self._current_view = MainView(
            self._root,
            self._projects,
            handle_project_select=None,
            handle_project_add=project_service.create_project,
            handle_logout=self.logout,
        )
        self._current_view.pack()

    def show_login_view(self):
        """Näyttää kirjautumisnäkymän."""
        self.clear_view()
        self._current_view = LoginView(
            self._root,
            self.show_projects_view,
            self.show_register_view
        )
        self._current_view.pack()

    def show_register_view(self):
        """Näyttää rekisteröitymisnäkymän"""
        self.clear_view()
        self._current_view = RegisterView(
            self._root,
            self.show_login_view,
            self.show_login_view
        )
        self._current_view.pack()
    
    def logout(self):
        """Kirjaa käyttäjän ulos ja palauttaa näkymän kirjautumisnäkymäksi"""
        user_service.logout()
        self.show_login_view()
