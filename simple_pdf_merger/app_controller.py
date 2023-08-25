from tkinter.messagebox import showwarning, showerror, showinfo
from tkinter.filedialog import askdirectory
import file_merger
from log_writer import write_log
from app_view import render_gui, update_display_output

def initialize(app, gui, log):
	default_output = "Nenhuma pasta selecionada"	

	app.set_title("Simple PDF Merger")
	gui.master.title(app.title)
	set_actions(app, gui, log)
	render_gui(gui)
	update_display_output(
		gui.origin_display,
		default_output
	)
	update_display_output(
		gui.destination_display,
		default_output
	)
	gui.mainloop()

def set_actions(app, gui, log):
	def set_origin(): 
		path = get_path("Selecione uma pasta com arquivos a unificar")

		app.set_path("origin", path)
		update_display_output(
			gui.origin_display,
			path
		)
		write_log(log, f"Origin path: {path}")
		

	def set_destination(): 
		path = get_path("Selecione uma pasta de destino")

		app.set_path("destination", path)
		update_display_output(
			gui.destination_display,
			path
		)

		write_log(log, f"Destination path: {path}")

	def merge_files():
		selection_status = check_selection(app)

		if selection_status == False: return

		file_merger.initialize(
			app.origin_path, 
			app.destination_path,
			log
		)		

		info_message = f"Seus arquivos foram unificados com sucesso. Você pode encontrá-los em {app.destination_path}"

		showinfo(
			title = "Operação concluída.",
			message = info_message
   		)

	gui.origin_button.configure(command = set_origin)
	gui.destination_button.configure(command = set_destination)
	gui.merge_button.configure(command = merge_files)

def get_path(message):
	return askdirectory(title = message)

def render_selection_error(target):
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
	
	if origin_status == None or origin_status == "":
		render_selection_error("origin")
		return False

	if destination_status == None or destination_status == "":
		render_selection_error("destination")	
		return False

	return True

