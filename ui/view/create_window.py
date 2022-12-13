import socket
import uuid

from PyQt6.QtWidgets import QMainWindow, QApplication

from enums import Role, Attempts
from ui.base.create_window import Ui_CreateWindow
import ui.view


class CreateWindow(QMainWindow, Ui_CreateWindow):
    def __init__(self, player: socket.socket):
        super().__init__()
        self.game_window = None
        self.message = None
        self.player = player

        self.setupUi(self)

        self.create_button.clicked.connect(self.create_game)

    def create_game(self):
        if not(self.game_name_input.text() and self.guessing_word_input.text()) and not self.message:
            self.message_label.setText("Fill all inputs!")
        else:
            game_name = self.game_name_input.text()
            game_name = f'{game_name}#{str(uuid.uuid4())[:4]}'
            guessing_word = self.guessing_word_input.text()
            attempts = int(self.attempts_number_choises.currentText())
            self.player.send(f'create;{game_name};{guessing_word};{attempts}'.encode('ascii'))

            self.game_window = ui.view.GameWindow(self.player, game_name, Role.leading,
                                                  guessing_word, Attempts(attempts))
            self.game_window.restoreGeometry(self.saveGeometry())
            self.game_window.show()
            self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = CreateWindow()

    window.show()
    app.exec()