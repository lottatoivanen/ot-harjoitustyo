from tkinter import ttk, constants

class ProjectView:
    def __init__(self, root, project, handle_back, handle_delete, handle_edit):
        self._root = root
        self._project = project
        self._handle_back = handle_back
        self._handle_delete = handle_delete
        self._handle_edit = handle_edit
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(self._frame, text=self._project.name, font=("Arial", 16, "bold"))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        desc_label = ttk.Label(self._frame, text=self._project.description, wraplength=400, font=("Arial", 12))
        desc_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        if self._project.user:
            owner = ttk.Label(self._frame, text=f"Owner: {self._project.user.username}")
            owner.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
    
        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        back_button.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)

        edit_button = ttk.Button(
            master=self._frame,
            text="Edit",
            command=lambda: self._handle_edit(self._project)
        )
        edit_button.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete",
            command=lambda: self._handle_delete(self._project)
        )
        delete_button.grid(row=4, column=1, padx=5, pady=5, sticky=constants.W)