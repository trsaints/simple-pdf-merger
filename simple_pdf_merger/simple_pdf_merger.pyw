from controller import app_controller
from models.app import App
from models.app_gui import AppGUI

app = App()
gui = AppGUI()

app_controller.initialize(app, gui)
