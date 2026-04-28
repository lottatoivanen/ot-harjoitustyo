from tkinter import Tk
from src.initialize_database import create_tables
from src.ui.ui import UI

create_tables()

window = Tk()
window.title("Muskaali- ja näytelmäprojekti sovellus")

window.minsize(width=500, height=400)

ui = UI(window)
ui.start()

window.mainloop()
