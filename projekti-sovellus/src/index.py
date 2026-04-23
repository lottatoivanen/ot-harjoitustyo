from tkinter import Tk
from src.initialize_database import create_tables
from src.ui.ui import UI

create_tables()

window = Tk()
window.title("Muskaali- ja näytelmäprojekti sovellus")

window.geometry("500x400")
window.minsize(400, 300)

ui = UI(window)
ui.start()

window.mainloop()
