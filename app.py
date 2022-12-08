import sys

from PyQt6.QtWidgets import QApplication

from ui.view import *

if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
