import tkinter as tk
from components.app_fonts import insert_fonts
from components.app_widgets import insert_widgets

class AppGUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(
            self,
            master,
            bg="#e2dfe0",
            padx=12,
            pady=6
        )

        self = insert_fonts(self)
        self = insert_widgets(self)