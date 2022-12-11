import socket

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import QtWidgets, QtCore, QtGui

from ui.base.start_window import Ui_StartWindow  # starting window in start_window.py
from ui.base.game_window import Ui_GameWindow  # game window in game_window.py
from ui.view.create_window import CreateWindow
from ui.view.game_window import GameWindow

HOST = '127.0.0.1'
PORT = 5060


class StartWindow(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.create_window = None
        self.game_window = None
        self.setupUi(self)

        self.player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player.connect(('127.0.0.1', 5060))

        self.new_game.clicked.connect(self.create_game)

        self.receive_games()

    def receive_games(self):
        games_str = self.player.recv(1024).decode('ascii')

        for game in games_str.split():
            self.withdraw_game(game)

    def withdraw_game(self, game_name):
        new_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        new_label.setMaximumSize(QtCore.QSize(16777215, 20))
        new_label.setObjectName(game_name)
        new_label.setStyleSheet("border: none;")

        button = QPushButton('JOIN', new_label)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(8)
        button.setFont(font)
        button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("background: rgb(31, 44, 56);\n"
                             "border-radius: 3;\n"
                             "color: white;\n"
                             "margin-left: 550px;"
                             "width: 50px;")

        button.clicked.connect(lambda checked, gn=game_name: self.join_game(gn))

        _translate = QtCore.QCoreApplication.translate
        new_label.setText(_translate("StartWindow", "Game name: " + game_name))
        self.verticalLayout.addWidget(new_label)

    def create_game(self):
        self.create_window = CreateWindow(self.player)

        self.create_window.show()
        self.close()

    def join_game(self, gn):
        self.player.send('join'.encode('ascii'))
        self.player.send(gn.encode('ascii'))

        self.game_window = GameWindow()
        self.game_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()

    window.show()
    app.exec()
