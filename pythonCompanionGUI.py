# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythonCompanion.ui'
#
# Created: Fri Feb 28 11:07:34 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(380, 20, 200, 200))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.albumLabel = QtGui.QLabel(self.centralwidget)
        self.albumLabel.setGeometry(QtCore.QRect(40, 60, 300, 14))
        self.albumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.albumLabel.setObjectName(_fromUtf8("albumLabel"))
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(40, 40, 300, 14))
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.artistLabel = QtGui.QLabel(self.centralwidget)
        self.artistLabel.setGeometry(QtCore.QRect(40, 20, 300, 14))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.artistLabel.setFont(font)
        self.artistLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.artistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.artistLabel.setObjectName(_fromUtf8("artistLabel"))
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(150, 90, 83, 24))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(270, 90, 83, 24))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.previousButton = QtGui.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(30, 90, 83, 24))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Companion", None))
        self.albumLabel.setText(_translate("MainWindow", "Album", None))
        self.titleLabel.setText(_translate("MainWindow", "Title", None))
        self.artistLabel.setText(_translate("MainWindow", "Artist", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))
        self.previousButton.setText(_translate("MainWindow", "Previous", None))

