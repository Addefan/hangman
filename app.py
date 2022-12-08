from PyQt6.QtWidgets import QMainWindow, QApplication

from ui.start_window import Ui_StartWindow # starting window in start_window.py
from ui.game_window import Ui_GameWindow   # game window in game_window.py

HOST = '127.0.0.1'
PORT = 5060


class StartWindow(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.setupUi(self)


class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    # app = QApplication([])
    # window = StartWindow()
    #
    # window.show()
    # app.exec()
    pass
