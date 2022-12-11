import socket
import threading
from os.path import join

from PyQt6 import QtWidgets, QtCore, QtGui

from ui.base import Ui_GameWindow


class GameWindow(QtWidgets.QMainWindow, Ui_GameWindow):
    attempts_stages = {13: (19, 37, 47, 56, 70, 78, 94, 165, 179, 188, 199, 206, 214),
                       12: (19, 37, 47, 56, 70, 94, 165, 179, 188, 199, 206, 214),
                       11: (19, 56, 70, 78, 94, 165, 179, 188, 199, 206, 214),
                       10: (19, 70, 78, 94, 165, 179, 188, 199, 206, 214),
                       9: (19, 56, 78, 94, 165, 179, 199, 206, 214),
                       8: (19, 56, 78, 94, 165, 179, 199, 214),
                       7: (19, 56, 94, 165, 179, 199, 214),
                       6: (56, 94, 165, 179, 199, 214)}
    stage = 0

    class SignalReceiver(QtCore.QObject):
        gif_paused = QtCore.pyqtSignal(int)
        game_finished = QtCore.pyqtSignal()

    def __init__(self, player, room_name, role, guessed_word, attempts):
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.room_name = room_name
        self.role = role.capitalize()
        self.guessed_word = guessed_word.upper()
        self.attempts = attempts
        self.game_is_over = False

        self.gif = QtGui.QMovie(join("ui", "media", "hangman.gif"), QtCore.QByteArray(), self)
        self.gif_label.setMovie(self.gif)
        self.setWindowTitle(f"Hangman - {self.room_name}")
        self.role_input.setText(self.role)
        self.maximum_mistakes.display(self.attempts)
        if self.role == "Leading":
            self.letters.setDisabled(True)
        for number, letter in enumerate(self.guessed_word):
            self.add_letter_to_screen(number)
        self.signal_receiver = self.SignalReceiver()

        self.signal_receiver.game_finished.connect(self.finish_game)
        self.signal_receiver.gif_paused.connect(self.set_gif_pause)
        self.gif.frameChanged.connect(self.gif_frame_changed)
        for letter in range(65, 91):
            self.__getattribute__(chr(letter)).clicked.connect(
                lambda: self.player.send(self.sender().text().encode('ascii')))

        self.receiver = threading.Thread(target=self.receive)
        self.receiver.start()

    def finish_game(self):
        self.game_is_over = True
        QtCore.QTimer.singleShot(500, lambda: self.hide())

    def set_gif_pause(self, set_pause: bool):
        self.gif.setPaused(set_pause)

    def add_letter_to_screen(self, number, symbol="　"):
        label_name = f"letter_{number}"
        self.__setattr__(label_name, QtWidgets.QLabel(self.word))
        self.__getattribute__(label_name).setMinimumSize(QtCore.QSize(32, 32))
        self.__getattribute__(label_name).setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setUnderline(True)
        self.__getattribute__(label_name).setFont(font)
        self.__getattribute__(label_name).setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.__getattribute__(label_name).setObjectName(label_name)
        self.horizontalLayout_5.addWidget(self.__getattribute__(label_name))
        self.__getattribute__(label_name).setText(symbol)

    def letter_button_clicked(self, letter):
        button = self.__getattribute__(letter)
        button.setEnabled(False)
        if button.text() not in self.guessed_word:
            button.setStyleSheet("background-color:rgba(255, 0, 0, 150);")
            self.current_mistakes.display(self.current_mistakes.value() + 1)
            self.stage += 1
            self.signal_receiver.gif_paused.emit(0)
            if self.current_mistakes.value() == self.maximum_mistakes.value():
                self.letters.setEnabled(False)
        else:
            button.setStyleSheet("background-color:rgba(0, 255, 0, 150);")
            for number, letter in enumerate(self.guessed_word):
                if letter == button.text():
                    self.__getattribute__(f"letter_{number}").setText(letter)
            self.guessed_word = self.guessed_word.replace(button.text(), "_")
            if set(self.guessed_word) == {"_"}:
                self.letters.setEnabled(False)
                self.signal_receiver.game_finished.emit()

    def gif_frame_changed(self, v):
        if v == self.gif.frameCount() - 1:
            self.gif.stop()
            self.signal_receiver.game_finished.emit()
        elif v == self.attempts_stages[self.attempts][self.stage - 1]:
            self.signal_receiver.gif_paused.emit(1)

    def resizeEvent(self, event):
        self.gif.setScaledSize(QtCore.QSize(self.gif_label.height(), self.gif_label.height()))

    def receive(self):
        while not self.game_is_over:
            try:
                letter = self.player.recv(1024).decode('ascii')
                self.letter_button_clicked(letter)
            except Exception as exc:
                print(exc)
                self.close()
