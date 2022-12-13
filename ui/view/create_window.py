import socket

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel

from ui.base.create_window import Ui_GameCreateWindow
import ui.view


class CreateWindow(QMainWindow, Ui_GameCreateWindow):
    def __init__(self, player: socket.socket):
        super().__init__()
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
            game_name, guessing_word = self.game_name.text(), self.guessing_word.text()
            self.player.send(f'create;{game_name};{guessing_word}'.encode('ascii'))

            self.game_window = ui.view.GameWindow(self.player, game_name, 'leading',
                                                  guessing_word, 6)
            self.game_window.show()
            self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = CreateWindow()

    window.show()
    app.exec()