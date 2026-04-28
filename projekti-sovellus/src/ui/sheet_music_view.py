import tkinter as tk
from tkinter import ttk, constants
from PIL import Image, ImageTk
import fitz

class SheetMusicView:
    def __init__(self, root, music, handle_back):
        self._root = root
        self._music = music
        self._handle_back = handle_back
        self._frame = None
        self._canvas = None
        self._scrollbar = None
        self._inner_frame = None
        self._images = []
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _render_pdf(self):
        doc = None
        try:
            doc = fitz.open(self._music.file_path)

            for page_index in range(len(doc)):
                page = doc.load_page(page_index)

                pix = page.get_pixmap()

                img = Image.frombytes(
                    "RGB",
                    (pix.width, pix.height),
                    pix.samples
                )

                tk_img = ImageTk.PhotoImage(img)

                label = ttk.Label(self._inner_frame, image=tk_img)
                label.image = tk_img
                label.pack(pady=10)

                self._images.append(tk_img)

        except Exception as error:
            ttk.Label(self._inner_frame, text=f"Error loading PDF: {error}").pack()
        finally:
            if doc is not None:
                doc.close()

    def _initialize(self):
        self._frame = ttk.Frame(self._root)

        header = ttk.Label(
            self._frame,
            text=f"{self._music.title}",
            font=("Arial", 16, "bold")
        )
        header.pack(anchor="w", padx=5, pady=5)

        back_btn = ttk.Button(
            self._frame,
            text="Back",
            command=self._handle_back
        )
        back_btn.pack(anchor="w", padx=5, pady=5)

        container = ttk.Frame(self._frame)
        container.pack(fill=constants.BOTH, expand=True)

        self._canvas = tk.Canvas(container, height=800)
        self._scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self._canvas.yview
        )

        self._inner_frame = ttk.Frame(self._canvas)

        self._inner_frame.bind(
            "<Configure>",
            lambda e: self._canvas.configure(
                scrollregion=self._canvas.bbox("all")
            )
        )
        self._canvas.create_window(
            (0, 0),
            window=self._inner_frame,
            anchor="nw"
        )
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._canvas.pack(side="left", fill=constants.BOTH, expand=True)
        self._scrollbar.pack(side="right", fill="y")
        self._render_pdf()