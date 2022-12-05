# Form implementation generated from reading ui file 'only_start.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(698, 409)
        StartWindow.setStyleSheet("background-color: rgb( 255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setStyleSheet("backgroud-color: rgb(215, 225, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(-10, -1, 711, 81))
        self.header.setStyleSheet("display: flex;\n"
"alig-items: center;")
        self.header.setObjectName("header")
        self.title = QtWidgets.QLabel(self.header)
        self.title.setGeometry(QtCore.QRect(275, 22, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(31, 44, 56)")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(-1, 79, 701, 331))
        self.container.setObjectName("container")
        self.rules = QtWidgets.QPushButton(self.container)
        self.rules.setGeometry(QtCore.QRect(589, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.rules.setFont(font)
        self.rules.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rules.setStyleSheet("background: rgb(31, 44, 56);\n"
"border-radius: 3;\n"
"color: white;\n"
"")
        self.rules.setObjectName("rules")
        self.new_game = QtWidgets.QPushButton(self.container)
        self.new_game.setGeometry(QtCore.QRect(29, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.new_game.setFont(font)
        self.new_game.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_game.setStyleSheet("background: rgb(31, 44, 56);\n"
"border-radius: 3;\n"
"color: white;\n"
"")
        self.new_game.setObjectName("new_game")
        self.games_title = QtWidgets.QLabel(self.container)
        self.games_title.setGeometry(QtCore.QRect(250, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        self.games_title.setFont(font)
        self.games_title.setStyleSheet("color: rgb(31, 44, 56)")
        self.games_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.games_title.setOpenExternalLinks(False)
        self.games_title.setObjectName("games_title")
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.title.setText(_translate("StartWindow", "HANGMAN"))
        self.rules.setText(_translate("StartWindow", "RULES"))
        self.new_game.setText(_translate("StartWindow", "NEW GAME"))
        self.games_title.setText(_translate("StartWindow", "JOIN GAMES"))
