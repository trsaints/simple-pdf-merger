import tkinter as tk
import tkinter.font as tk_font
from string import Template

class AppGUI(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(
			self, 
			master,
			bg = "#e2dfe0",
			padx = 12,
			pady = 6
		)

		self.create_fonts()
		self.create_widgets()
	
	def create_fonts(self):
		self.main_font = tk_font.Font(
			family = "Segoe UI", 
			size = 12, 
			weight = "normal"
		)
		self.main_font_bold = tk_font.Font(
			family = "Segoe UI",
			size = 12,
			weight = "bold"
		)
		self.mono_font = tk_font.Font(
			family = "Cascadia Mono",
			size = 9,
			weight = "normal"
		)	

	def create_widgets(self):
		self.origin_label_frame = tk.LabelFrame(
			self,
			labelanchor = "nw",
			font = self.main_font_bold,
			text = "Pasta de origem",
			bg = "#e2dfe0"
		)
		self.destination_label_frame = tk.LabelFrame(
			self,
			labelanchor = "nw",
			font = self.main_font_bold,
			text = "Pasta de destino",
			bg = "#e2dfe0"
		)
		self.origin_button = tk.Button(
			self.origin_label_frame, 
			text = "Selecionar pasta", 
			font = self.main_font, 
			bg = "#bcb3b3"
		)
		self.destination_button = tk.Button(
			self.destination_label_frame, 
			text = "Selecionar pasta", 
			font = self.main_font, 
			bg = "#bcb3b3"
		)
		self.merge_button = tk.Button(
			self, 
			text = "Unificar PDFs", 
			font = self.main_font, 
			bg = "#48bf84",
		)
		self.origin_display = tk.Text(
			self.origin_label_frame,
			font = self.mono_font,
			padx = 8,
			pady = 4,
			width = 100,
			height = 1,
			state = "disabled"
		)
		self.destination_display = tk.Text(
			self.destination_label_frame,
			font = self.mono_font,
			padx = 8,
			pady = 4,
			width = 100,
			height = 1,
			state = "disabled"
		)
