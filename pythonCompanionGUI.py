# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/welshy136/Desktop/Development/pythonCompanion/pythonCompanion.ui'
#
# Created: Sat Mar  8 15:03:33 2014
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
        MainWindow.resize(571, 246)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(0, 12, 0, 12)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.verticalLayout.addWidget(self.titleLabel)
        self.artistAlbumLabel = QtGui.QLabel(self.centralwidget)
        self.artistAlbumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.artistAlbumLabel.setObjectName(_fromUtf8("artistAlbumLabel"))
        self.verticalLayout.addWidget(self.artistAlbumLabel)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.timeLabel = QtGui.QLabel(self.centralwidget)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout_2.addWidget(self.timeLabel)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.durationLabel = QtGui.QLabel(self.centralwidget)
        self.durationLabel.setObjectName(_fromUtf8("durationLabel"))
        self.horizontalLayout_2.addWidget(self.durationLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previousButton = QtGui.QPushButton(self.centralwidget)
        self.previousButton.setEnabled(False)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.horizontalLayout.addWidget(self.previousButton)
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        self.playButton.setMinimumSize(QtCore.QSize(93, 0))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setEnabled(False)
        self.nextButton.setMinimumSize(QtCore.QSize(93, 0))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.artworkImg = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artworkImg.sizePolicy().hasHeightForWidth())
        self.artworkImg.setSizePolicy(sizePolicy)
        self.artworkImg.setMinimumSize(QtCore.QSize(200, 200))
        self.artworkImg.setFrameShape(QtGui.QFrame.Box)
        self.artworkImg.setText(_fromUtf8(""))
        self.artworkImg.setAlignment(QtCore.Qt.AlignCenter)
        self.artworkImg.setObjectName(_fromUtf8("artworkImg"))
        self.horizontalLayout_3.addWidget(self.artworkImg)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.previousButton, self.nextButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Companion", None))
        self.titleLabel.setText(_translate("MainWindow", "Title", None))
        self.artistAlbumLabel.setText(_translate("MainWindow", "Artist - Album", None))
        self.timeLabel.setText(_translate("MainWindow", "0:00", None))
        self.durationLabel.setText(_translate("MainWindow", "0:00", None))
        self.previousButton.setText(_translate("MainWindow", "Previous", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))

