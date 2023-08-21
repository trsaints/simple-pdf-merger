from tkinter.messagebox import showwarning, showerror, showinfo
from tkinter.filedialog import askdirectory
from string import Template
import file_merger

def initialize(app, gui, title):
	default_output = "Nenhuma pasta selecionada"

	gui.master.title(title)
	set_actions(app, gui)
	gui.render()
	gui.update_path_output(
		gui.origin_display,
		default_output
	)
	gui.update_path_output(
		gui.destination_display,
		default_output
	)
	gui.mainloop()

def set_actions(app, gui):
	def set_origin(): 
		path = get_path("Selecione a pasta com arquivos a unificar")
		app.set_path("origin", path)
		gui.update_path_output(
			gui.origin_display,
			path
		)

	def set_destination(): 
		path = get_path("Selecione a pasta de destino")
		app.set_path("destination", path)
		gui.update_path_output(
			gui.destination_display,
			path
		)

	def merge_files():
		selection_status = check_selection(app)

		if selection_status == False: return

		file_merger.initialize(
			origin = app.origin_path, 
			destination = app.destination_path
		)		

		info_message = Template(
			"Seus arquivos foram unificados com sucesso. Você pode encontrá-los em ${destination}"
		).substitute(destination = app.destination_path)

		showinfo(
			title = "Operação concluída.",
			message = info_message
   		)

	gui.origin_button.configure(command = set_origin)
	gui.destination_button.configure(command = set_destination)
	gui.merge_button.configure(command = merge_files)

def get_path(message):
	return askdirectory(title = message)

def render_selection_error(self, target):		
	if target == "origin":
		showerror(
			title = "Falha ao unificar arquivos",
			message = "Nenhuma pasta de origem foi selecionada"
		)
	elif target == "destination":
		showerror(
			title = "Falha ao unificar arquivos",
			message = "Nenhuma pasta de destino foi selecionada"
		)
	
def check_selection(app):
	origin_status = getattr(app, "origin_path", None)
	destination_status = getattr(app, "destination_path", None)
	
	if origin_status == None:
		render_selection_error("origin")
		return False

	if destination_status == None:
		render_selection_error("destination")	
		return False

	return True

