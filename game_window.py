# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GameWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 559)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setAccessibleName("")
        self.frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(43, 10, 32, 32))
        self.label_2.setMinimumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(76, 10, 32, 32))
        self.label_5.setMinimumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setTabletTracking(False)
        self.label_5.setAcceptDrops(False)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(108, 10, 32, 32))
        self.label_6.setMinimumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setTabletTracking(False)
        self.label_6.setAcceptDrops(False)
        self.label_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(141, 10, 32, 32))
        self.label_7.setMinimumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setTabletTracking(False)
        self.label_7.setAcceptDrops(False)
        self.label_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setEnabled(False)
        self.label_13.setMinimumSize(QtCore.QSize(200, 200))
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(32, 32))
        self.label_8.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(32, 32))
        self.label_9.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setMinimumSize(QtCore.QSize(32, 32))
        self.label_10.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setMinimumSize(QtCore.QSize(32, 32))
        self.label_11.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setMinimumSize(QtCore.QSize(32, 32))
        self.label_12.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_79 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_79.setEnabled(False)
        self.pushButton_79.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setAutoFillBackground(False)
        self.pushButton_79.setStyleSheet("background: rgb(255, 0, 0)")
        self.pushButton_79.setCheckable(False)
        self.pushButton_79.setChecked(False)
        self.pushButton_79.setAutoExclusive(False)
        self.pushButton_79.setObjectName("pushButton_79")
        self.horizontalLayout.addWidget(self.pushButton_79)
        self.pushButton_80 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_80.setEnabled(False)
        self.pushButton_80.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_80.setAutoFillBackground(False)
        self.pushButton_80.setStyleSheet("background: rgb(0, 255, 0)")
        self.pushButton_80.setObjectName("pushButton_80")
        self.horizontalLayout.addWidget(self.pushButton_80)
        self.pushButton_81 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_81.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_81.setObjectName("pushButton_81")
        self.horizontalLayout.addWidget(self.pushButton_81)
        self.pushButton_82 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_82.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_82.setObjectName("pushButton_82")
        self.horizontalLayout.addWidget(self.pushButton_82)
        self.pushButton_83 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_83.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_83.setObjectName("pushButton_83")
        self.horizontalLayout.addWidget(self.pushButton_83)
        self.pushButton_84 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_84.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_84.setObjectName("pushButton_84")
        self.horizontalLayout.addWidget(self.pushButton_84)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_120 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_120.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_120.setObjectName("pushButton_120")
        self.horizontalLayout_3.addWidget(self.pushButton_120)
        self.pushButton_118 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_118.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_118.setObjectName("pushButton_118")
        self.horizontalLayout_3.addWidget(self.pushButton_118)
        self.pushButton_122 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_122.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_122.setObjectName("pushButton_122")
        self.horizontalLayout_3.addWidget(self.pushButton_122)
        self.pushButton_123 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_123.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_123.setObjectName("pushButton_123")
        self.horizontalLayout_3.addWidget(self.pushButton_123)
        self.pushButton_124 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_124.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_124.setObjectName("pushButton_124")
        self.horizontalLayout_3.addWidget(self.pushButton_124)
        self.pushButton_119 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_119.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_119.setObjectName("pushButton_119")
        self.horizontalLayout_3.addWidget(self.pushButton_119)
        self.pushButton_121 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_121.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_121.setObjectName("pushButton_121")
        self.horizontalLayout_3.addWidget(self.pushButton_121)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_112 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_112.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_112.setObjectName("pushButton_112")
        self.horizontalLayout_2.addWidget(self.pushButton_112)
        self.pushButton_117 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_117.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_117.setObjectName("pushButton_117")
        self.horizontalLayout_2.addWidget(self.pushButton_117)
        self.pushButton_116 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_116.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_116.setObjectName("pushButton_116")
        self.horizontalLayout_2.addWidget(self.pushButton_116)
        self.pushButton_113 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_113.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_113.setObjectName("pushButton_113")
        self.horizontalLayout_2.addWidget(self.pushButton_113)
        self.pushButton_114 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_114.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_114.setObjectName("pushButton_114")
        self.horizontalLayout_2.addWidget(self.pushButton_114)
        self.pushButton_111 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_111.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_111.setObjectName("pushButton_111")
        self.horizontalLayout_2.addWidget(self.pushButton_111)
        self.pushButton_115 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_115.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_115.setObjectName("pushButton_115")
        self.horizontalLayout_2.addWidget(self.pushButton_115)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_130 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_130.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_130.setObjectName("pushButton_130")
        self.horizontalLayout_4.addWidget(self.pushButton_130)
        self.pushButton_125 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_125.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_125.setObjectName("pushButton_125")
        self.horizontalLayout_4.addWidget(self.pushButton_125)
        self.pushButton_128 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_128.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_128.setObjectName("pushButton_128")
        self.horizontalLayout_4.addWidget(self.pushButton_128)
        self.pushButton_126 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_126.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_126.setObjectName("pushButton_126")
        self.horizontalLayout_4.addWidget(self.pushButton_126)
        self.pushButton_129 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_129.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_129.setObjectName("pushButton_129")
        self.horizontalLayout_4.addWidget(self.pushButton_129)
        self.pushButton_127 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_127.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_127.setObjectName("pushButton_127")
        self.horizontalLayout_4.addWidget(self.pushButton_127)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.lcdNumber_4.setFont(font)
        self.lcdNumber_4.setDigitCount(2)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_4.setProperty("intValue", 12)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.lcdNumber_3.setFont(font)
        self.lcdNumber_3.setDigitCount(2)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_3.setProperty("intValue", 1)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "　"))
        self.label_2.setText(_translate("MainWindow", "　"))
        self.label_5.setText(_translate("MainWindow", "　"))
        self.label_6.setText(_translate("MainWindow", "　"))
        self.label_7.setText(_translate("MainWindow", "　"))
        self.label_8.setText(_translate("MainWindow", "　"))
        self.label_9.setText(_translate("MainWindow", "B"))
        self.label_10.setText(_translate("MainWindow", "　"))
        self.label_11.setText(_translate("MainWindow", "　"))
        self.label_12.setText(_translate("MainWindow", "　"))
        self.pushButton_79.setText(_translate("MainWindow", "A"))
        self.pushButton_80.setText(_translate("MainWindow", "B"))
        self.pushButton_81.setText(_translate("MainWindow", "C"))
        self.pushButton_82.setText(_translate("MainWindow", "D"))
        self.pushButton_83.setText(_translate("MainWindow", "E"))
        self.pushButton_84.setText(_translate("MainWindow", "F"))
        self.pushButton_120.setText(_translate("MainWindow", "N"))
        self.pushButton_118.setText(_translate("MainWindow", "O"))
        self.pushButton_122.setText(_translate("MainWindow", "P"))
        self.pushButton_123.setText(_translate("MainWindow", "Q"))
        self.pushButton_124.setText(_translate("MainWindow", "R"))
        self.pushButton_119.setText(_translate("MainWindow", "S"))
        self.pushButton_121.setText(_translate("MainWindow", "T"))
        self.pushButton_112.setText(_translate("MainWindow", "G"))
        self.pushButton_117.setText(_translate("MainWindow", "H"))
        self.pushButton_116.setText(_translate("MainWindow", "I"))
        self.pushButton_113.setText(_translate("MainWindow", "J"))
        self.pushButton_114.setText(_translate("MainWindow", "K"))
        self.pushButton_111.setText(_translate("MainWindow", "L"))
        self.pushButton_115.setText(_translate("MainWindow", "M"))
        self.pushButton_130.setText(_translate("MainWindow", "U"))
        self.pushButton_125.setText(_translate("MainWindow", "V"))
        self.pushButton_128.setText(_translate("MainWindow", "W"))
        self.pushButton_126.setText(_translate("MainWindow", "X"))
        self.pushButton_129.setText(_translate("MainWindow", "Y"))
        self.pushButton_127.setText(_translate("MainWindow", "Z"))
        self.label_3.setText(_translate("MainWindow", "/"))
        self.label_4.setText(_translate("MainWindow", "Mistakes:"))
