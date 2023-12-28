from app import App
from app_gui import AppGUI
from app_controller import initialize

app = App()
gui = AppGUI()

initialize(app, gui)
