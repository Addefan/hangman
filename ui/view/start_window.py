import json
import socket
import threading

from PyQt6.QtWidgets import QMainWindow, QApplication

from ui.base.start_window import Ui_StartWindow # starting window in start_window.py
from ui.base.game_window import Ui_GameWindow   # game window in game_window.py
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

        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

    def receive(self):
        is_games_received = False

        while True:
            try:
                if is_games_received:
                    pass
                else:
                    games_str = self.player.recv(2048).decode('ascii')
                    is_games_received = True
                    games = json.loads(games_str)
                    for game in games.keys():
                        print(game)
            except Exception as exc:
                print(exc)
                self.close()

    # def withdraw_game(self):
    #     self.game_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.game_label.setGeometry(QtCore.QRect(10, 9, 621, 31))
    #     self.game_label.setStyleSheet("background: rgb(221, 226, 255)")
    #     self.game_label.setObjectName("game_label")
    #     self.Connect = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
    #     self.Connect.setGeometry(QtCore.QRect(553, 15, 71, 20))
    #     self.Connect.setStyleSheet("background: rgb(31, 44, 56);\n"
    #                                "border-radius: 3;\n"
    #                                "color: white;\n"
    #                                "")
    #     self.Connect.setObjectName("Connect")
    #     self.scroll_games.setWidget(self.scrollAreaWidgetContents)
    #     StartWindow.setCentralWidget(self.centralwidget)
    #
    #     _translate = QtCore.QCoreApplication.translate
    #     self.game_label.setText(_translate("StartWindow", "Game label"))
    #     self.Connect.setText(_translate("StartWindow", "CONNECT"))

    def open_game_window(self):
        self.game = GameWindow()
        self.close()
        self.game.show()


if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()

    window.show()
    app.exec()
