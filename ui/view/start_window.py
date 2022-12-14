import os
import socket
import threading

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import QtWidgets, QtCore, QtGui

from enums import Role
from ui.base.start_window import Ui_StartWindow  # starting window in start_window.py
import ui.view

HOST = '127.0.0.1'
PORT = 5060


class StartWindow(QMainWindow, Ui_StartWindow):
    class Signaller(QObject):
        added_game = pyqtSignal(str)
        finished = pyqtSignal()

    def __init__(self):
        super(StartWindow, self).__init__()
        self.start_window = None
        self.create_window = None
        self.game_window = None
        self.setupUi(self)
        self.stop = False
        self.lock = threading.Lock()

        self.player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player.connect(('127.0.0.1', 5060))

        self.new_game.clicked.connect(self.create_game)

        self.signaller = self.Signaller()
        self.signaller.added_game.connect(self.withdraw_game)

        self.receive_games()

        self.update_button.clicked.connect(self.refresh_window)

        # self.thread = threading.Thread(name='New games receiver', target=self.receive_new_game)
        # self.thread.start()

    def receive_games(self):
        games_str = self.player.recv(1024).decode('ascii')

        for game in games_str.split():
            self.withdraw_game(game)

    # def receive_new_game(self):
    #     while True:
    #         if self.stop:
    #             break
    #         game = self.player.recv(1024).decode('ascii')
    #         print(game)
    #         self.signaller.added_game.emit(game)

    def withdraw_game(self, game_name):
        frame = QtWidgets.QFrame(self.games)
        frame.setObjectName(game_name)

        layout = QtWidgets.QHBoxLayout(frame)
        layout.setObjectName(f"{game_name}_layout")

        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)

        label = QtWidgets.QLabel(frame)
        label.setObjectName(f"{game_name}_label")
        label.setFont(font)
        label.setText(f"Game name: {game_name}")

        button = QtWidgets.QPushButton(frame)
        button.setObjectName(f"{game_name}_button")
        button.setFont(font)
        button.setText("Join")

        layout.addWidget(label)
        layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addWidget(frame)

        button.clicked.connect(lambda checked, gn=game_name: self.join_game(gn))

    def create_game(self):
        self.stop = True

        self.create_window = ui.view.CreateWindow(self.player)
        self.create_window.restoreGeometry(self.saveGeometry())
        for th in threading.enumerate():
            print(th)
        self.create_window.show()
        self.close()

    def join_game(self, gn):
        self.stop = True

        self.player.send(f'join;{gn}'.encode('ascii'))
        guessing_word = self.player.recv(1024).decode('ascii')

        self.game_window = ui.view.GameWindow(self.player, gn, Role.guesser, guessing_word, 6)
        self.game_window.restoreGeometry(self.saveGeometry())
        self.game_window.show()
        self.close()

    def refresh_window(self):
        self.player.close()
        self.start_window = __class__()
        self.start_window.restoreGeometry(self.saveGeometry())
        self.start_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()

    window.show()
    app.exec()
