import tkinter as tk
import tkinter.font as tk_font
from tkinter.filedialog import askdirectory
import merge_pdf_files as file_merger

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master
)
		self.main_font = tk_font.Font(family='Segoe UI', size=14, weight='normal')

		self.grid()
		self.create_widgets()
		self.render_widgets()

	def create_widgets(self):
		self.origin_button = tk.Button(self, text='Selecionar pasta de origem', font=self.main_font, command=self.get_origin_directory)
		self.destination_button = tk.Button(self, text='Selecionar pasta de destino', font=self.main_font, command=self.get_destination_directory)
		self.merge_button = tk.Button(self, text='Unificar PDFs', font=self.main_font, command = self.merge_files)

	def render_widgets(self):	
		self.origin_button.grid(
			row=0, column=2, columnspan=3, padx=12, pady=8, sticky=tk.E+tk.W
		)
		self.destination_button.grid(
			row=1, column=2, columnspan=3, padx=12, pady=8, sticky=tk.E+tk.W
	)
		self.merge_button.grid(
			row=2, column=2, columnspan=3, padx=12, pady=8, sticky=tk.E+tk.W
		)

	def get_origin_directory(self):
		self.origin_path = askdirectory(title='Selecione a pasta com os arquivos a serem unificados')
		print(self.origin_path)

	def get_destination_directory(self):
		self.destination_path = askdirectory(title='Selecione onde deseja armazenar os arquivos unificados')
		print(self.destination_path)

	def merge_files(self):
		file_merger.initialize(
			origin=self.origin_path, 
			destination=self.destination_path
		)		

app = Application()
app.master.title('PDF Merger')
app.mainloop()
