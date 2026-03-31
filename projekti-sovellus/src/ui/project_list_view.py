from tkinter import ttk, constants

class ProjectListView:
    """Projektien listauksesta vastaava näkymä."""

    def __init__(self, root, projects, handle_project_select):
        self._root = root
        self._projects = projects
        self._handle_project_select = handle_project_select
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_project_item(self, project):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=project)

        select_button = ttk.Button(
            master=item_frame,
            text="Valitse",
            command=lambda: self._handle_project_select(project)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        select_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for project in self._projects:
            self._initialize_project_item(project)
