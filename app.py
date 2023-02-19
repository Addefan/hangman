import ctypes
import sys
from os.path import join

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

import ui.view

if __name__ == "__main__":
    appid = 'hangman.1.0.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    app = QApplication([])
    app.setWindowIcon(QIcon(join("ui", "media", "hangman_icon.png")))
    window = ui.view.StartWindow()

    window.show()
    sys.exit(app.exec())
