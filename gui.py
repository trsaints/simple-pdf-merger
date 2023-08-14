import tkinter as tk
import tkinter.font as tk_font
import merge_pdf_files as file_merger
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning, showerror, showinfo
from string import Template

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(
			self, 
			master,
			bg="#e2dfe0"
		)

		self.main_font = tk_font.Font(
			family='Segoe UI', 
			size=14, 
			weight='normal'
		)

		self.grid()
		self.create_widgets()
		self.render_widgets()

	def create_widgets(self):
		self.origin_button = tk.Button(
			self, 
			text='Selecionar pasta de origem', 
			font=self.main_font, 
			command=self.get_origin_directory,
			bg="#bcb3b3"
		)
		self.destination_button = tk.Button(
			self, 
			text='Selecionar pasta de destino', 
			font=self.main_font, 
			command=self.get_destination_directory,
			bg="#bcb3b3"
		)
		self.merge_button = tk.Button(
			self, 
			text='Unificar PDFs', 
			font=self.main_font, 
			command = self.merge_files,
			bg="#48bf84"
		)

	def render_widgets(self):	
		self.origin_button.grid(
			row=0, 
			column=2, 
			columnspan=3, 
			padx=12, 
			pady=8, 
			sticky=tk.E+tk.W
		)
		self.destination_button.grid(
			row=1, 
			column=2, 
			columnspan=3, 
			padx=12, 
			pady=8, 
			sticky=tk.E+tk.W
		)
		self.merge_button.grid(
			row=2, 
			column=2, 
			columnspan=3, 
			padx=12, 
			pady=8, 
			sticky=tk.E+tk.W
		)

	def get_origin_directory(self):
		self.origin_path = askdirectory(title='Selecione a pasta com os arquivos a serem unificados')
		message = Template("Origin folder: ${origin}").substitute(origin=self.origin_path)

		print(message)

	def get_destination_directory(self):
		self.destination_path = askdirectory(title='Selecione onde deseja armazenar os arquivos unificados')
		message = Template("Destination folder: ${destination}").substitute(destination=self.destination_path)

		print(message)

	def render_selection_error(self, target):		
		if target == "origin":
			showerror(
				title="Falha ao unificar arquivos",
				message="Nenhuma pasta de origem foi selecionada"
			)

		if target == "destination":
			showerror(
				title="Falha ao unificar arquivos",
				message="Nenhuma pasta de destino foi selecionada"
			)
	
	def check_selection(self):
		origin_status = getattr(self, "origin_path", None)
		destination_status = getattr(self, "destination_path", None)	

		if origin_status == None:
			self.render_selection_error("origin")
			return False

		if destination_status == None:
			self.render_selection_error("destination")	
			return False

		return True

	def merge_files(self):
		selection_status = self.check_selection()

		if selection_status == False: return

		file_merger.initialize(
			origin=self.origin_path, 
			destination=self.destination_path
		)		

