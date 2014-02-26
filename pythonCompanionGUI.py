# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Welshy136\Desktop\pythonCompanion.ui'
#
# Created: Tue Feb 25 12:11:13 2014
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
        MainWindow.resize(691, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(390, 20, 200, 200))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.albumLabel = QtGui.QLabel(self.centralwidget)
        self.albumLabel.setGeometry(QtCore.QRect(40, 60, 300, 14))
        self.albumLabel.setObjectName(_fromUtf8("albumLabel"))
        self.albumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(40, 40, 300, 14))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.artistLabel = QtGui.QLabel(self.centralwidget)
        self.artistLabel.setGeometry(QtCore.QRect(40, 20, 300, 14))
        self.artistLabel.setObjectName(_fromUtf8("artistLabel"))
        self.artistLabel.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.albumLabel.setText(_translate("MainWindow", "Album", None))
        self.titleLabel.setText(_translate("MainWindow", "Title", None))
        self.artistLabel.setText(_translate("MainWindow", "Artist", None))

