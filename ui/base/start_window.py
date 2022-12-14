# Form implementation generated from reading ui file 'start_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(587, 562)
        StartWindow.setStyleSheet("QPushButton{background:rgb(31, 44, 56);border-radius:3px;color:white;padding:4px;margin:4px;}QPushButton:hover{border:1px solid white;}QPushButton:pressed{color:black;background:white;}QScrollArea{border:3px solid rgb(31, 44, 56);border-radius:3px;}")
        self.main_widget = QtWidgets.QWidget(StartWindow)
        self.main_widget.setStyleSheet("backgroud-color: rgb(215, 225, 255)")
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setText("Hangman")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.new_game = QtWidgets.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.new_game.setFont(font)
        self.new_game.setObjectName("new_game")
        self.buttons_layout.addWidget(self.new_game, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.update_button = QtWidgets.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.update_button.setFont(font)
        self.update_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.update_button.setStyleSheet("")
        self.update_button.setObjectName("update_button")
        self.buttons_layout.addWidget(self.update_button, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addLayout(self.buttons_layout)
        self.games_title = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.games_title.setFont(font)
        self.games_title.setStyleSheet("")
        self.games_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.games_title.setOpenExternalLinks(False)
        self.games_title.setObjectName("games_title")
        self.verticalLayout_2.addWidget(self.games_title)
        self.scrollArea = QtWidgets.QScrollArea(self.main_widget)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 563, 418))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.games = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.games.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.games.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.games.setObjectName("games")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.games)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addWidget(self.games, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        StartWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Hangman"))
        self.new_game.setText(_translate("StartWindow", "New game"))
        self.update_button.setText(_translate("StartWindow", "Refresh games"))
        self.games_title.setText(_translate("StartWindow", "Join games"))
