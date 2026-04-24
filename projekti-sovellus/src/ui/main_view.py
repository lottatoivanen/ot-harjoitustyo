import tkinter as tk
from tkinter import ttk, constants, messagebox
from src.ui.project_list_view import ProjectListView
from src.ui.add_project_view import AddProjectView
from src.ui.project_view import ProjectView
from src.ui.edit_project_view import EditProjectView
from src.entities.project import Project
from src.services.user_service import user_service
from src.services.date_service import date_service
from src.repositories.project_repository import project_repository

DATE_TYPE_OPTIONS = ("Practice", "Performance", "Other")

class MainView:
    """Projektien listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root, projects, handle_project_select, handle_project_add, handle_logout):
        self._root = root
        self._projects = projects
        self._handle_project_select = handle_project_select
        self._handle_project_add = handle_project_add
        self._handle_logout = handle_logout
        self._user = user_service.get_current_user()
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
            text="Projects",
            font=("Arial", 16, "bold")
        )
        header.pack(anchor="w", padx=5, pady=5)

        self._project_list_view = ProjectListView(
            self._current_view,
            self._projects,
            self._show_project_view
        )
        self._project_list_view.render()

        add_button = ttk.Button(
            master=self._current_view,
            text="Add project",
            command=self._show_add_project_view
        )
        add_button.pack(anchor="w", padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._current_view,
            text="Logout",
            command=self._handle_logout
        )
        logout_button.pack(anchor="ne", padx=5, pady=5)
    
    def _show_project_view(self, project):
        self._clear_view()

        self._current_view = ProjectView(
            root=self._content_frame,
            project=project,
            handle_back=self._show_projects_view,
            handle_delete=self._delete_project,
            handle_edit=self._edit_project,
            handle_add_date=self._add_project_date,
            handle_delete_date=self._delete_project_date,
        )

        self._current_view.pack()
    
    def _delete_project(self, project):
        if not messagebox.askyesno("Confirm delete", f"Delete project: '{project.name}'?"):
            return
        project_repository.delete(project.id)
        self._projects = [p for p in self._projects if p.id != project.id]
        self._show_projects_view()
    
    def _edit_project(self, project):
        self._clear_view()
        self._current_view = EditProjectView(
            root=self._content_frame,
            project=project,
            handle_project_update=self._handle_project_edit,
            handle_cancel=self._show_projects_view
        )
        self._current_view.grid()
    
    def _handle_project_edit(self, project, name, description):
        project.name = name
        project.description = description
        project_repository.update(project)
        self._show_projects_view()

    def _add_project_date(self, project, date_str, date_type):
        parsed_date = date_service(date_str)
        if not parsed_date:
            return False

        normalized_type = date_type if date_type in DATE_TYPE_OPTIONS else "Practice"
        project.dates.append({"type": normalized_type, "date": parsed_date})
        project_repository.update(project)
        return True

    def _delete_project_date(self, project, date_index):
        if date_index < 0 or date_index >= len(project.dates):
            return False

        project.dates.pop(date_index)
        project_repository.update(project)
        return True

    def _show_add_project_view(self):
        self._clear_view()

        self._current_view = AddProjectView(
            root=self._content_frame,
            handle_project_add=self._handle_project_add_and_return,
            handle_cancel=self._show_projects_view
        )
        self._current_view.grid()

    def _handle_project_add_and_return(self, project_name, project_desc):
        project_name = project_name.strip()
        project_desc = project_desc.strip()
        if not project_name:
            return
        if self._handle_project_add:
            new_project = self._handle_project_add(project_name, project_desc)
        else:
            new_project = Project(name=project_name, description=project_desc, user=None)
        self._projects.append(new_project)

        self._show_projects_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._content_frame = ttk.Frame(master=self._frame)
        self._content_frame.pack(fill=constants.BOTH, expand=True)
        self._show_projects_view()