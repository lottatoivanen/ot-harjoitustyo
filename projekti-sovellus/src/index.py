from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Muskaali- ja näytelmäprojekti sovellus")

ui = UI(window)
ui.start()

window.mainloop()