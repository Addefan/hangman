from PyQt6.QtWidgets import QMainWindow

from ui.base.game_window import Ui_GameWindow


class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setupUi(self)