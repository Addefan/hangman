from PyQt6 import QtWidgets

from ui.base import Ui_EndWindow
from ui.view import StartWindow


class EndWindow(QtWidgets.QMainWindow, Ui_EndWindow):
    def __init__(self, player, message):
        super().__init__()
        self.setupUi(self)

        self.start_window = None
        self.player = player
        self.message = message

        self.message_label.setText(message)

        self.go_menu.clicked.connect(self.go_to_menu)

    def go_to_menu(self):
        self.player.close()
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()
