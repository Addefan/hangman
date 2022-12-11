import socket

from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel

from ui.base.create_window import Ui_GameCreateWindow
from ui.view import GameWindow


class CreateWindow(QMainWindow, Ui_GameCreateWindow):
    def __init__(self, player: socket.socket):
        super(CreateWindow, self).__init__()
        self.game_window = None
        self.message = None
        self.player = player

        self.setupUi(self)

        self.create_button.clicked.connect(self.create_game)

    def create_game(self):
        if not(self.game_name.text() and self.guessing_word.text()) and not self.message:
            self.message = QLabel(f"Fill all inputs!")
            self.verticalLayout.addWidget(self.message)
        else:
            self.player.send('create'.encode('ascii'))
            self.player.send(self.game_name.text().encode('ascii'))
            self.player.send(self.guessing_word.text().encode('ascii'))
            
            self.game_window = GameWindow()
            self.game_window.show()
            self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = CreateWindow()

    window.show()
    app.exec()