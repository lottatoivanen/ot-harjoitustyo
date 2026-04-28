from tkinter import ttk, constants

class ProjectListView:
    """Näkymä, joka vastaa projektien listaamisesta"""

    def __init__(self, root, projects, handle_project_select):
        self._root = root
        self._projects = projects
        self._handle_project_select = handle_project_select
        self._frame = None

        self._initialize()

    def render(self):
        """Näyttää näkymän."""
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_project_item(self, project):
        """Luo komponentit tietylle projektille listassa"""
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=project.name)

        select_button = ttk.Button(
            master=item_frame,
            text="Open",
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
        """Luo näkymän komponentit."""
        self._frame = ttk.Frame(master=self._root)

        for project in self._projects:
            self._initialize_project_item(project)
