import tkinter as tk
from tkinter.messagebox import showerror


def render_gui(gui):
    gui.origin_button.grid(
        row=0,
        column=2,
        columnspan=3,
        padx=12,
        pady=8,
        ipadx=8,
        sticky=tk.E+tk.W
    )
    gui.destination_button.grid(
        row=1,
        column=2,
        columnspan=3,
        padx=12,
        pady=8,
        ipadx=8,
        sticky=tk.E+tk.W
    )
    gui.merge_button.grid(
        row=2,
        column=0,
        columnspan=3,
        padx=12,
        pady=8,
        sticky=tk.E+tk.W
    )
    gui.origin_display.grid(
        row=0,
        column=1,
        padx=12,
        pady=8
    )
    gui.destination_display.grid(
        row=1,
        column=1,
        padx=12,
        pady=8
    )
    gui.origin_label_frame.grid(
        row=0,
        column=1,
        padx=12,
        pady=8,
        sticky=tk.NW
    )
    gui.destination_label_frame.grid(
        row=1,
        column=1,
        padx=12,
        pady=8,
        sticky=tk.NW
    )
    gui.grid(sticky=tk.N+tk.E+tk.S+tk.W)

    set_default_folder_output(gui)


def update_display_output(display, output):
    display.configure(state="normal")
    display.delete("1.00", "end")
    display.insert("end", output)
    display.configure(state="disabled")


def render_selection_error(selection):
    if selection == "origin":
        showerror(
            title="Falha ao unificar arquivos",
            message="Nenhuma pasta de origem foi selecionada"
        )
    elif selection == "destination":
        showerror(
            title="Falha ao unificar arquivos",
            message="Nenhuma pasta de destino foi selecionada"
        )


def set_default_folder_output(gui):
    default_output = "Nenhuma pasta selecionada"

    update_display_output(
        gui.origin_display,
        default_output
    )
    update_display_output(
        gui.destination_display,
        default_output
    )
