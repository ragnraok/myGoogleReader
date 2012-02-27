# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rss_feed_dialog.ui'
#
# Created: Fri Feb 10 22:59:04 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_rssFeedDialog(object):
    def setupUi(self, rssFeedDialog):
        rssFeedDialog.setObjectName(_fromUtf8("rssFeedDialog"))
        rssFeedDialog.resize(427, 122)
        self.pushButton = QtGui.QPushButton(rssFeedDialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 80, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(rssFeedDialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 401, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(rssFeedDialog)
        QtCore.QMetaObject.connectSlotsByName(rssFeedDialog)

    def retranslateUi(self, rssFeedDialog):
        rssFeedDialog.setWindowTitle(QtGui.QApplication.translate("rssFeedDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("rssFeedDialog", "确定", None, QtGui.QApplication.UnicodeUTF8))

