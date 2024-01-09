import tkinter.font as tk_font


def insert_fonts(self):
    updated_self = self

    updated_self.main_font = tk_font.Font(
        updated_self,
        family="Segoe UI",
        size=12,
        weight="normal"
    )
    updated_self.main_font_bold = tk_font.Font(
        updated_self,
        family="Segoe UI",
        size=12,
        weight="bold"
    )
    updated_self.mono_font = tk_font.Font(
        updated_self,
        family="Cascadia Mono",
        size=9,
        weight="normal"
    )

    return updated_self
