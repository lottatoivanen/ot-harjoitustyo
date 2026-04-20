from tkinter import Tk
from initialize_database import create_tables
from ui.ui import UI

create_tables()

window = Tk()
window.title("Muskaali- ja näytelmäprojekti sovellus")

ui = UI(window)
ui.start()

window.mainloop()
