import tkinter as tk
from tkinter import ttk, constants

class AddProjectView:
    """Näkymä, joka mahdollistaa uuden projektin lisäämisen."""

    def __init__(self, root, handle_project_add, handle_cancel):
        self._root = root
        self._handle_project_add = handle_project_add
        self._handle_cancel = handle_cancel
        self._frame = None
        self._project_name_entry = None

        self._initialize()

    def grid(self):
        """Näyttää näkymän."""
        self._frame.grid(sticky=constants.EW)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _add_project(self):
        """Käsittelee projektin lisäämisen."""
        project_name = self._project_name_entry.get().strip()
        project_desc = self._project_desc_entry.get("1.0", "end").strip()
        if project_name:
            self._handle_project_add(project_name, project_desc)

    def _initialize(self):
        """Luo näkymän komponentit."""
        self._frame = ttk.Frame(master=self._root)

        title_label = ttk.Label(
            master=self._frame,
            text="Add project",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        
        name_label = ttk.Label(
            master=self._frame,
            text="Project name:",
            font=("Arial", 12)
        )
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._project_name_entry = ttk.Entry(master=self._frame)
        self._project_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=constants.EW)

        desc_label = ttk.Label(
            master=self._frame,
            text="Description:",
            font=("Arial", 12)
        )
        desc_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._project_desc_entry = tk.Text(
            master=self._frame,
            height=5,
            width=40
            )
        self._project_desc_entry.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

        add_button = ttk.Button(
            master=self._frame,
            text="Add",
            command=self._add_project
        )
        add_button.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)

        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._handle_cancel
        )
        cancel_button.grid(row=3, column=1, padx=5, pady=5, sticky=constants.E)
        self._frame.grid_columnconfigure(1, weight=1)
