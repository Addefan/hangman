import json
import socket
import threading

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets, QtCore

from ui.base.start_window import Ui_StartWindow  # starting window in start_window.py
from ui.base.game_window import Ui_GameWindow  # game window in game_window.py
from ui.view.game_window import GameWindow

HOST = '127.0.0.1'
PORT = 5060


class StartWindow(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.setupUi(self)

        self.player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player.connect(('127.0.0.1', 5060))

        self.new_game.clicked.connect(self.open_game_window)

        self.receive_games()

    def receive_games(self):
        games_str = self.player.recv(2048).decode('ascii')

        for game in games_str.split():
            self.withdraw_game(game)

    def withdraw_game(self, game_name):
        new_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        new_label.setMaximumSize(QtCore.QSize(16777215, 25))
        new_label.setObjectName(game_name)

        _translate = QtCore.QCoreApplication.translate
        new_label.setText(_translate("StartWindow", game_name))
        self.verticalLayout.addWidget(new_label)

    def open_game_window(self):
        self.game = GameWindow()
        self.close()
        self.game.show()


if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()

    window.show()
    app.exec()
