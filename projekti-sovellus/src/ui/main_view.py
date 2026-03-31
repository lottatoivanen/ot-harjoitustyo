from tkinter import ttk, constants
from ui.project_list_view import ProjectListView

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

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        label = ttk.Label(
            master=self._frame,
            text="Projektit",
            font=("Arial", 16)
        )
        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

    def _handle_create_project(self):
        project_name = self._create_project_entry.get().strip()

        if not project_name:
            return
        if project_name in self._projects:
            return

        self._projects.append(project_name)
        self._initialize_project_list()
        self._create_project_entry.delete(0, constants.END)
        self._handle_project_add(project_name)

    def _initialize_footer(self):
        self._create_project_entry = ttk.Entry(master=self._frame)

        add_button = ttk.Button(
            master=self._frame,
            text="Lisää projekti",
            command=self._handle_create_project
        )

        self._create_project_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        add_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize_project_list(self):
        if self._project_list_view:
            self._project_list_view.destroy()

        self._project_list_view = ProjectListView(
            self._project_list_frame,
            self._projects,
            self._handle_project_select
        )
        self._project_list_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._project_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_project_list()
        self._initialize_footer()

        self._project_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)