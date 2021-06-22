# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ddownloader\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 102)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 40, 361, 20))
        self.status.setObjectName("status")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 60, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 365, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_url = QtWidgets.QLineEdit(self.widget)
        self.input_url.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_url.sizePolicy().hasHeightForWidth())
        self.input_url.setSizePolicy(sizePolicy)
        self.input_url.setMinimumSize(QtCore.QSize(250, 0))
        self.input_url.setObjectName("input_url")
        self.horizontalLayout.addWidget(self.input_url)
        self.btn_download = QtWidgets.QPushButton(self.widget)
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout.addWidget(self.btn_download)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "臭 DD 下載器"))
        self.status.setText(_translate("MainWindow", "Ready"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.input_url.setText(_translate("MainWindow", "https://youtu.be/1G8I_WPwd1Q"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
from . import main_rc
