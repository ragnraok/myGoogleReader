# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Feb 10 14:34:13 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(775, 584)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.contentList = QtGui.QListView(self.centralwidget)
        self.contentList.setGeometry(QtCore.QRect(270, 0, 511, 541))
        self.contentList.setObjectName(_fromUtf8("contentList"))
        self.sourceLIst = QtGui.QListView(self.centralwidget)
        self.sourceLIst.setGeometry(QtCore.QRect(-5, 0, 271, 541))
        self.sourceLIst.setObjectName(_fromUtf8("sourceLIst"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUser = QtGui.QMenu(self.menubar)
        self.menuUser.setObjectName(_fromUtf8("menuUser"))
        self.menuRSS = QtGui.QMenu(self.menubar)
        self.menuRSS.setObjectName(_fromUtf8("menuRSS"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.loginAction = QtGui.QAction(MainWindow)
        self.loginAction.setObjectName(_fromUtf8("loginAction"))
        self.exitAction = QtGui.QAction(MainWindow)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.subAction = QtGui.QAction(MainWindow)
        self.subAction.setObjectName(_fromUtf8("subAction"))
        self.menuUser.addAction(self.loginAction)
        self.menuUser.addAction(self.exitAction)
        self.menuRSS.addAction(self.subAction)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuRSS.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUser.setTitle(QtGui.QApplication.translate("MainWindow", "用户", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRSS.setTitle(QtGui.QApplication.translate("MainWindow", "RSS", None, QtGui.QApplication.UnicodeUTF8))
        self.loginAction.setText(QtGui.QApplication.translate("MainWindow", "登陆", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setText(QtGui.QApplication.translate("MainWindow", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.subAction.setText(QtGui.QApplication.translate("MainWindow", "订阅", None, QtGui.QApplication.UnicodeUTF8))

