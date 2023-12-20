from app import App
from app_gui import AppGUI
from app_controller import initialize
from log_writer import open_log

app = App()
gui = AppGUI()
process_log = open_log('./log/process.txt')

initialize(app, gui, process_log)
