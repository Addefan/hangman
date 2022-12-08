from PyQt6 import QtWidgets

from ui.base import Ui_StartWindow


class StartWindow(QtWidgets.QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
