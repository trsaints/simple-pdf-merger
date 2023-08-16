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
			size=12, 
			weight='normal'
		)
		self.main_font_bold = tk_font.Font(
			family="Segoe UI",
			size=12,
			weight="bold"
		)
		self.mono_font = tk_font.Font(
			family='Cascadia Mono',
			size=10,
			weight='normal'
		)

		self.grid()
		self.create_widgets()
		self.render_widgets()

	def create_widgets(self):
		self.origin_label_frame = tk.LabelFrame(
			self,
			labelanchor="nw",
			font=self.main_font_bold,
			text="Pasta de origem",
			bg="#e2dfe0"
		)
		self.destination_label_frame = tk.LabelFrame(
			self,
			labelanchor="nw",
			font=self.main_font_bold,
			text="Pasta de destino",
			bg="#e2dfe0"
		)
		self.origin_button = tk.Button(
			self.origin_label_frame, 
			text='Selecionar pasta', 
			font=self.main_font, 
			command=self.set_origin,
			bg="#bcb3b3"
		)
		self.destination_button = tk.Button(
			self.destination_label_frame, 
			text='Selecionar pasta', 
			font=self.main_font, 
			command=self.set_destination,
			bg="#bcb3b3"
		)
		self.merge_button = tk.Button(
			self, 
			text='Unificar PDFs', 
			font=self.main_font, 
			command = self.merge_files,
			bg="#48bf84"
		)
		self.origin_display = tk.Text(
			self.origin_label_frame,
			font=self.mono_font,
			padx=8,
			pady=4,
			width=128,
			height=1,
			state="disabled"
		)
		self.destination_display = tk.Text(
			self.destination_label_frame,
			font=self.mono_font,
			padx=8,
			pady=4,
			width=128,
			height=1,
			state="disabled"
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
			column=0, 
			columnspan=3, 
			padx=12, 
			pady=8, 
			sticky=tk.E+tk.W
		)
		self.origin_display.grid(
			row=0,
			column=5,
			padx=12,
			pady=8,
		)
		self.destination_display.grid(
			row=1,
			column=5,
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

	def get_path_message(self, target):
		if target == "origin":
			return "Selecione a pasta com os arquivos a serem unificados"
		elif target == "destination":
			return "Selecione a pasta de destino"
	
		return ""
	
	def get_path(self, target):
		dialog_message = self.get_path_message(target)
		target_path = askdirectory(title=dialog_message)
		return target_path

	def set_path(self, target):
		target_path = self.get_path(target)
		
		if target == "origin":
			self.origin_path = target_path
		elif target == "destination":
			self.destination_path = target_path

	def update_path_display(self, target, path):
		target.configure(state = "normal")
		target.delete(
			"1.00",
			"end"
		)
		target.insert(
			"end",
			path
		)
		target.configure(state = "disabled")

	def set_origin(self):
		self.set_path("origin")
		self.update_path_display(self.origin_display, self.origin_path)

	def set_destination(self):
		self.set_path("destination")
		self.update_path_display(self.destination_display, self.destination_path)	
	
	def render_selection_error(self, target):		
		if target == "origin":
			showerror(
				title="Falha ao unificar arquivos",
				message="Nenhuma pasta de origem foi selecionada"
			)
		elif target == "destination":
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

		info_message = Template("Seus arquivos foram unificados com sucesso. Você pode encontrá-los em ${destination}").substitute(destination = self.destination_path)

		showinfo(
			title="Operação concluída.",
			message=info_message
        )
