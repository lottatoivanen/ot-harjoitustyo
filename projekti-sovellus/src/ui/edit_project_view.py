import tkinter as tk
from tkinter import ttk, constants

class EditProjectView:
    """Näkymä, joka mahdollistaa projektin muokkaamisen."""

    def __init__(self, root, project, handle_project_update, handle_cancel):
        self._root = root
        self._project = project
        self._handle_project_update = handle_project_update
        self._handle_cancel = handle_cancel
        self._frame = None
        self._project_name_entry = None

        self._initialize()

    def grid(self):
        self._frame.grid(sticky=constants.EW)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title_lavel = ttk.Label(
            master=self._frame,
            text="Edit project",
            font=("Arial", 16, "bold")
        )
        title_lavel.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        
        name_label = ttk.Label(
            master=self._frame,
            text="Project name:",
            font=("Arial", 12)
        )
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._project_name_entry = ttk.Entry(master=self._frame)
        self._project_name_entry.insert(0, self._project.name)
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
        self._project_desc_entry.insert("1.0", self._project.description)
        self._project_desc_entry.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

        save_button = ttk.Button(
            master=self._frame,
            text="Save",
            command=self._update_project
        )
        save_button.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)

        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._handle_cancel
        )
        cancel_button.grid(row=3, column=1, padx=5, pady=5, sticky=constants.E)
        self._frame.grid_columnconfigure(1, weight=1)
    
    def _update_project(self):
        project_name = self._project_name_entry.get().strip()
        project_desc = self._project_desc_entry.get("1.0", "end").strip()
        if project_name:
            self._handle_project_update(self._project, project_name, project_desc)