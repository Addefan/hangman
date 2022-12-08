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

    def __init__(self, room_name, role, guessed_word, attempts):
        super().__init__()
        self.setupUi(self)
        self.room_name = room_name
        self.role = role.capitalize()
        self.guessed_word = guessed_word.upper()
        self.attempts = attempts

        self.gif = QtGui.QMovie(join("ui", "media", "hangman.gif"), QtCore.QByteArray(), self)
        self.gif_label.setMovie(self.gif)
        self.setWindowTitle(f"Hangman - {self.room_name}")
        self.role_input.setText(self.role)
        self.maximum_mistakes.display(self.attempts)
        if self.role == "Leading":
            self.letters.setDisabled(True)
        for number, letter in enumerate(self.guessed_word):
            self.add_letter_to_screen(number)

        self.gif.frameChanged.connect(self.gif_frame_changed)
        for letter in range(65, 91):
            self.__getattribute__(chr(letter)).clicked.connect(self.letter_button_clicked)

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

    def letter_button_clicked(self):
        button = self.sender()
        button.setEnabled(False)
        if button.text() not in self.guessed_word:
            button.setStyleSheet("background-color:rgba(255, 0, 0, 150);")
            self.current_mistakes.display(self.current_mistakes.value() + 1)
            self.stage += 1
            self.gif.setPaused(False)
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
                QtCore.QTimer.singleShot(500, lambda: self.hide())

    def gif_frame_changed(self, v):
        if v == self.gif.frameCount() - 1:
            self.gif.stop()
            QtCore.QTimer.singleShot(500, lambda: self.hide())
        elif v == self.attempts_stages[self.attempts][self.stage - 1]:
            self.gif.setPaused(True)

    def resizeEvent(self, event):
        self.gif.setScaledSize(QtCore.QSize(self.gif_label.height(), self.gif_label.height()))
