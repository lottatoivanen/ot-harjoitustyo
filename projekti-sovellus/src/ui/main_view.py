import tkinter as tk
from tkinter import ttk, constants
from ui.project_list_view import ProjectListView
from ui.add_project_view import AddProjectView

class MainView:
    """Projektien listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root, projects, handle_project_select, handle_project_add):
        self._root = root
        self._projects = projects
        self._handle_project_select = handle_project_select
        self._handle_project_add = handle_project_add
        self._frame = None
        self._project_list_frame = None
        self._project_list_view = None
        self._create_project_entry = None
        self._current_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _clear_view(self):
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None
    
    def _show_projects_view(self):
        self._clear_view()

        self._current_view = ttk.Frame(master=self._content_frame)
        self._current_view.pack(fill=constants.BOTH, expand=True)

        header = ttk.Label(
            master=self._current_view,
            text="Projektit",
            font=("Arial", 16)
        )
        header.pack(anchor="w", padx=5, pady=5)

        self._project_list_view = ProjectListView(
            self._current_view,
            self._projects,
            self._handle_project_select
        )
        self._project_list_view.render()

        add_button = ttk.Button(
            master=self._current_view,
            text="Lisää projekti",
            command=self._show_add_project_view
        )
        add_button.pack(anchor="e", padx=5, pady=5)

    def _show_add_project_view(self):
        self._clear_view()

        self._current_view = AddProjectView(
            root=self._content_frame,
            handle_project_add=self._handle_project_add_and_return,
            handle_cancel=self._show_projects_view
        )
        self._current_view.grid()

    def _handle_project_add_and_return(self, project_name):
        project_name = project_name.strip()
        if project_name and project_name not in self._projects:
            self._projects.append(project_name)
            self._handle_project_add(project_name)

        self._show_projects_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # A single container for all subviews
        self._content_frame = ttk.Frame(master=self._frame)
        self._content_frame.pack(fill=constants.BOTH, expand=True)

        # Show default view
        self._show_projects_view()