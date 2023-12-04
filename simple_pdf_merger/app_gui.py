import tkinter as tk
from app_fonts import insert_fonts
from app_widgets import insert_widgets


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

    def render(self):
        self.origin_button.grid(
            row=0,
            column=2,
            columnspan=3,
            padx=12,
            pady=8,
            ipadx=8,
            sticky=tk.E+tk.W
        )
        self.destination_button.grid(
            row=1,
            column=2,
            columnspan=3,
            padx=12,
            pady=8,
            ipadx=8,
            sticky=tk.E+tk.W
        )
        self.merge_button.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=12,
            pady=8,
            sticky=tk.E+tk.W
        )
        self.origin_display.grid(
            row=0,
            column=1,
            padx=12,
            pady=8,
        )
        self.destination_display.grid(
            row=1,
            column=1,
            padx=12,
            pady=8,
        )
        self.origin_label_frame.grid(
            row=0,
            column=1,
            padx=12,
            pady=8,
            sticky=tk.NW
        )
        self.destination_label_frame.grid(
            row=1,
            column=1,
            padx=12,
            pady=8,
            sticky=tk.NW
        )
        self.grid(sticky=tk.N+tk.E+tk.S+tk.W)

    def update_path_output(self, target, text):
        target.configure(state="normal")
        target.delete(
            "1.00",
            "end"
        )
        target.insert(
            "end",
            text
        )
        target.configure(state="disabled")
