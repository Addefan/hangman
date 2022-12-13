import sys

from PyQt6.QtWidgets import QApplication

import ui.view

if __name__ == "__main__":
    app = QApplication([])
    window = ui.view.StartWindow()
    window.move(0, 0)  # левый верхний
    # window.move(QGuiApplication.primaryScreen().availableGeometry().width() - window.width(), 0)    # правый верхний

    window.show()
    sys.exit(app.exec())
