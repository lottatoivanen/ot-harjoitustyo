from tkinter import Tk
from src.ui.ui import UI

window = Tk()
window.title("Muskaali- ja näytelmäprojekti sovellus")

window.minsize(width=500, height=400)

ui = UI(window)
ui.start()

window.mainloop()
