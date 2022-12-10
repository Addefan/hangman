from PyQt6.QtWidgets import QApplication

from ui.view import *

if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()
    window.move(0, 0)  # левый верхний
    # window.move(QGuiApplication.primaryScreen().availableGeometry().width() - window.width(), 0)    # правый верхний

    window.show()
    app.exec()
