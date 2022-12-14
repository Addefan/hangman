import ctypes
import sys
from os.path import join

from PyQt6.QtGui import QGuiApplication, QIcon
from PyQt6.QtWidgets import QApplication

import ui.view

if __name__ == "__main__":
    appid = 'hangman.1.0.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    app = QApplication([])
    app.setWindowIcon(QIcon(join("ui", "media", "hangman_icon.png")))
    window = ui.view.StartWindow()

    window.move(0, 0)  # левый верхний
    # window.move(QGuiApplication.primaryScreen().availableGeometry().width() - window.width(), 0)    # правый верхний

    window.show()
    sys.exit(app.exec())
