from ui.main_view import MainView
from ui.login_view import LoginView
from ui.register_view import RegisterView

class UI:
    """Sovelluksen pääkäyttöliittymä, joka sisältää päävalikon ja projektinäkymän."""
    def __init__(self, root):
        self._root = root
        self._projects = []
        self._current_view = None

    def start(self):
        self.show_login_view()

    def clear_view(self):
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None

    def show_projects_view(self):
        self.clear_view()
        self._current_view = MainView(
            self._root,
            self._projects,
            self.on_project_selected,
            self.on_project_added
        )
        self._current_view.pack()

    def show_login_view(self):
        self.clear_view()
        self._current_view = LoginView(
            self._root,
            self.show_projects_view,
            self.show_register_view
        )
        self._current_view.pack()

    def show_register_view(self):
        self.clear_view()
        self._current_view = RegisterView(
            self._root,
            self.show_login_view,
            self.show_login_view
        )
        self._current_view.pack()

    def on_project_selected(self, project):
        print(f"Valittu projekti: {project}")

    def on_project_added(self, project):
        print(f"Lisätty projekti: {project}")
