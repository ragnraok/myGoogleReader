# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rss_content.ui'
#
# Created: Fri Feb 10 14:34:52 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(597, 458)
        self.rssContentView = QtWebKit.QWebView(Dialog)
        self.rssContentView.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.rssContentView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.rssContentView.setObjectName(_fromUtf8("rssContentView"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 50, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 100, 97, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "查看原文", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "关闭", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
