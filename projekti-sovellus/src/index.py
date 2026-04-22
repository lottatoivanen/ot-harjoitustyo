from tkinter import Tk
from initialize_database import create_tables
from ui.ui import UI

create_tables()

window = Tk()
window.title("Muskaali- ja näytelmäprojekti sovellus")

window.geometry("500x400")
window.minsize(400, 300)

ui = UI(window)
ui.start()

window.mainloop()
