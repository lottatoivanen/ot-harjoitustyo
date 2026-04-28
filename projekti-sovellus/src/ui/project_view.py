from tkinter import ttk, constants, messagebox

DATE_TYPE_OPTIONS = ("Practice", "Performance", "Other")

class ProjectView:
    """Näkymä projektin tarkastelulle"""

    def __init__(self, root, project, handle_back, handle_delete, handle_edit, handle_add_date, handle_delete_date, handle_music):
        self._root = root
        self._project = project
        self._handle_back = handle_back
        self._handle_delete = handle_delete
        self._handle_edit = handle_edit
        self._handle_open_music = handle_music
        self._on_add_date = handle_add_date
        self._on_delete_date = handle_delete_date
        self._frame = None
        self._date_entry = None
        self._date_type_combobox = None
        self._dates_frame = None
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.Y)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _add_date(self):
        """Lisää tärkeitä päivämääriä projektille"""
        date_str = self._date_entry.get()
        date_type = self._date_type_combobox.get().strip()

        if not date_str:
            messagebox.showerror("Error", "Please enter a valid date")
            return

        if not date_type:
            messagebox.showerror("Error", "Please select a date type")
            return

        if self._on_add_date(self._project, date_str, date_type):
            self._date_entry.delete(0, constants.END)
            self._date_type_combobox.set("Other")
            self._render_dates()
        else:
            messagebox.showerror("Error", "Please enter date in format dd.mm.yyyy or dd.mm.yyyy hh:mm")

    def _delete_date(self, date_index):
        """Poistaa projektin päivämäärän"""
        if not messagebox.askyesno("Confirm delete", "Delete this date?"):
            return

        if self._on_delete_date(self._project, date_index):
            self._render_dates()

    def _render_dates(self):
        """Tuhoaa vanhat päivämääräkomponentit ja luo uudet projektin päivämäärien perusteella."""
        for widget in self._dates_frame.winfo_children():
            widget.destroy()

        if not self._project.dates:
            ttk.Label(self._dates_frame, text="No dates added").pack(anchor=constants.W)
            return

        for index, date_entry in enumerate(self._project.dates):
            row = ttk.Frame(self._dates_frame)
            row.pack(anchor=constants.W, fill=constants.X, pady=2)

            date_type = date_entry.get("type", "Other")
            date_value = date_entry.get("date")

            if not date_value:
                continue

            label = ttk.Label(
                row,
                text=f"{date_type}: {date_value.strftime('%d.%m.%Y %H:%M')}"
            )
            label.grid(row=0, column=0, sticky=constants.W)

            delete_button = ttk.Button(
                row,
                text="Delete",
                command=lambda i=index: self._delete_date(i)
            )
            delete_button.grid(row=0, column=1, padx=5, sticky=constants.W)
    
    def _handle_music(self):
        """Näyttää näkymän, jossa tarkasellaan projektin nuotteja."""
        self._handle_open_music(self._project)

    def _initialize(self):
        """Luo näkymän komponentit."""
        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(self._frame, text=self._project.name, font=("Arial", 16, "bold"))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        desc_label = ttk.Label(self._frame, text=self._project.description, wraplength=400, font=("Arial", 12))
        desc_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        if self._project.user:
            owner = ttk.Label(self._frame, text=f"Owner: {self._project.user.username}", font=("Arial", 12, "italic"))
            owner.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        back_button.grid(row=2, column=9, padx=5, pady=5, sticky=constants.E)

        edit_button = ttk.Button(
            master=self._frame,
            text="Edit",
            command=lambda: self._handle_edit(self._project)
        )
        edit_button.grid(row=0, column=9, padx=5, pady=5, sticky=constants.E)

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete",
            command=lambda: self._handle_delete(self._project)
        )
        delete_button.grid(row=1, column=9, padx=5, pady=5, sticky=constants.E)

        date_label = ttk.Label(
            self._frame,
            text="Add important dates",
            font=("Arial", 12, "bold")
        )
        date_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

        self._date_entry = ttk.Entry(master=self._frame)
        self._date_entry.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)

        date_button = ttk.Button(
            master=self._frame,
            text="Add date",
            command=self._add_date
        )
        date_button.grid(row=5, column=1, padx=5, pady=5, sticky=constants.W)

        self._date_type_combobox = ttk.Combobox(
            master=self._frame,
            values=DATE_TYPE_OPTIONS,
            state="readonly"
        )
        self._date_type_combobox.set("Practice")
        self._date_type_combobox.grid(row=6, column=0, padx=5, pady=5, sticky=constants.W)

        self._dates_frame = ttk.Frame(master=self._frame)
        self._dates_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=constants.W)
        self._render_dates()

        music_button = ttk.Button(
            master=self._frame,
            text="Manage Music",
            command=lambda: self._handle_open_music(self._project)
        )
        music_button.grid(row=3, column=9, padx=5, pady=5, sticky=constants.E)
