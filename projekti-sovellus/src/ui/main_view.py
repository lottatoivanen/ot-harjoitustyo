import tkinter as tk
from tkinter import ttk, constants, messagebox
from src.ui.project_list_view import ProjectListView
from src.ui.add_project_view import AddProjectView
from src.ui.project_view import ProjectView
from src.ui.edit_project_view import EditProjectView
from src.ui.music_view import MusicView
from src.ui.sheet_music_view import SheetMusicView
from src.entities.project import Project, Music
from src.services.user_service import user_service
from src.services.date_service import date_service
from src.repositories.project_repository import project_repository

DATE_TYPE_OPTIONS = ("Practice", "Performance", "Other")

class MainView:
    """Näkymä, jossa listataan käyttäjän projektit ja josta pääsee projektikohtaisiin näkymiin."""

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
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()
    
    def _clear_view(self):
        """Tuhoaa nykyisen näkymän, jos sellainen on."""
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None
    
    def _show_projects_view(self):
        """Näyttää näkymän, jossa listataan käyttäjän projektit."""
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
        """Näyttää näkymän, jossa tarkastellaan projektia ja sen tietoja."""
        self._clear_view()

        self._current_view = ProjectView(
            root=self._content_frame,
            project=project,
            handle_back=self._show_projects_view,
            handle_delete=self._delete_project,
            handle_edit=self._edit_project,
            handle_add_date=self._add_project_date,
            handle_delete_date=self._delete_project_date,
            handle_music=self._show_music_view,
        )

        self._current_view.pack()
    
    def _delete_project(self, project):
        """Varmistaa projektin poiston."""
        if not messagebox.askyesno("Confirm delete", f"Delete project: '{project.name}'?"):
            return
        project_repository.delete(project.id)
        self._projects = [p for p in self._projects if p.id != project.id]
        self._show_projects_view()
    
    def _edit_project(self, project):
        """Näyttää näkymän, jossa muokataan projektia."""
        self._clear_view()
        self._current_view = EditProjectView(
            root=self._content_frame,
            project=project,
            handle_project_update=self._handle_project_edit,
            handle_cancel=lambda: self._show_project_view(project)
        )
        self._current_view.grid()
    
    def _handle_project_edit(self, project, name, description):
        """Päivittää projektin tiedot ja palaa projektin tarkastelunäkymään."""
        project.name = name
        project.description = description
        project_repository.update(project)
        self._show_project_view(project)

    def _add_project_date(self, project, date_str, date_type):
        """Lisää projektin tärkeän päivämäärän."""
        parsed_date = date_service(date_str)
        if not parsed_date:
            return False

        normalized_type = date_type if date_type in DATE_TYPE_OPTIONS else "Practice"
        project.dates.append({"type": normalized_type, "date": parsed_date})
        project_repository.update(project)
        return True

    def _delete_project_date(self, project, date_index):
        """Poistaa projektin päivämäärän."""
        if date_index < 0 or date_index >= len(project.dates):
            return False

        project.dates.pop(date_index)
        project_repository.update(project)
        return True

    def _show_music_view(self, project):
        """Näyttää näkymän, jossa tarkastellaan projektin nuotteja"""
        self._clear_view()
        self._current_view = MusicView(
            root=self._content_frame,
            project=project,
            handle_back=lambda: self._show_project_view(project),
            handle_add_music=self._add_music_to_project,
            handle_delete_music=self._delete_music_from_project,
            handle_open_music=self._show_sheet_music
        )
        self._current_view.pack()

    def _add_music_to_project(self, project, title, file_path):
        """Lisää nuotin projektille."""
        new_music = Music(title=title, file_path=file_path)
        project.music_scores.append(new_music)
        project_repository.update(project)
        self._show_music_view(project)

    def _delete_music_from_project(self, project, music):
        """Poistaa nuotin projektilta"""
        project.music_scores.remove(music)
        project_repository.update(project)
        self._show_music_view(project)
        return True

    def _show_sheet_music(self, project, music):
        """Näyttää näkymän, jossa tarkastellaan nuottitiedostoa"""
        self._clear_view()
        self._current_view = SheetMusicView(
            self._content_frame,
            music,
            handle_back=lambda: self._show_music_view(project)
        )
        self._current_view.pack()

    def _show_add_project_view(self):
        """Näyttää näkymän, jossa lisätään projekti"""
        self._clear_view()

        self._current_view = AddProjectView(
            root=self._content_frame,
            handle_project_add=self._handle_project_add_and_return,
            handle_cancel=self._show_projects_view
        )
        self._current_view.grid()

    def _handle_project_add_and_return(self, project_name, project_desc):
        """Lisää projektin ja palaa projektien listausnäkymään."""
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
        """Luo näkymän komponentit."""
        self._frame = ttk.Frame(master=self._root)
        self._content_frame = ttk.Frame(master=self._frame)
        self._content_frame.pack(fill=constants.BOTH, expand=True)
        self._show_projects_view()