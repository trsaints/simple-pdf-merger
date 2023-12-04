import tkinter as tk


def insert_widgets(self):
    updated_self = self

    updated_self.origin_label_frame = tk.LabelFrame(
        updated_self,
        labelanchor="nw",
        font=updated_self.main_font_bold,
        text="Pasta de origem",
        bg="#e2dfe0"
    )
    updated_self.destination_label_frame = tk.LabelFrame(
        updated_self,
        labelanchor="nw",
        font=updated_self.main_font_bold,
        text="Pasta de destino",
        bg="#e2dfe0"
    )
    updated_self.origin_button = tk.Button(
        updated_self.origin_label_frame,
        text="Selecionar pasta",
        font=updated_self.main_font,
        bg="#bcb3b3"
    )
    updated_self.destination_button = tk.Button(
        updated_self.destination_label_frame,
        text="Selecionar pasta",
        font=updated_self.main_font,
        bg="#bcb3b3"
    )
    updated_self.merge_button = tk.Button(
        updated_self,
        text="Unificar PDFs",
        font=updated_self.main_font,
        bg="#48bf84",
    )
    updated_self.origin_display = tk.Text(
        updated_self.origin_label_frame,
        font=updated_self.mono_font,
        padx=8,
        pady=4,
        width=100,
        height=1,
        state="disabled"
    )
    updated_self.destination_display = tk.Text(
        updated_self.destination_label_frame,
        font=updated_self.mono_font,
        padx=8,
        pady=4,
        width=100,
        height=1,
        state="disabled"
    )

    return updated_self
