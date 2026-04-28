import tkinter as tk
from tkinter import ttk, constants, filedialog, messagebox
from os.path import basename

class MusicView:
    def __init__(self, root, project, handle_back, handle_add_music, handle_delete_music, handle_open_music):
        self._root = root
        self._project = project
        self._handle_back = handle_back
        self._handle_add_music = handle_add_music
        self._handle_delete_music = handle_delete_music
        self._handle_open_music = handle_open_music
        self._frame = None
        self._library_frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()
    
    def _add_music(self):
        file_path = filedialog.askopenfilename(
            title="Select sheet music file",
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            title = basename(file_path)
            self._handle_add_music(self._project, title, file_path)

    def _open_music(self, music):
        self._handle_open_music(self._project, music)
    
    def _delete_music(self, music):
        if not messagebox.askyesno("Confirm delete", f"Delete '{music.title}'?"):
            return
        self._handle_delete_music(self._project, music)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(
            master=self._frame,
            text=f"Sheet music for {self._project.name}",
            font=("Arial", 16, "bold")
        )
        header.pack(anchor="w", padx=5, pady=5)

        add_music_button = ttk.Button(
            master=self._frame,
            text="Add sheet music",
            command=self._add_music
        )
        add_music_button.pack(pady=10)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        back_button.pack(pady=10)

        container = ttk.Frame(self._frame)
        container.pack(fill=constants.BOTH, expand=True)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self._library_frame = ttk.Frame(canvas)
        self._library_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self._library_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill=constants.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        for music in self._project.music_scores:
            tile = ttk.Frame(self._library_frame)
            tile.pack(fill=constants.X, padx=5, pady=5)

            btn = ttk.Button(
                tile,
                text=f"📄 {music.title}",
                command=lambda: self._open_music(music)
            )
            btn.pack(side="left")

            delete_music_button = ttk.Button(
                tile,
                text="Delete",
                command=lambda: self._delete_music(music)
            )
            delete_music_button.pack(side="right")