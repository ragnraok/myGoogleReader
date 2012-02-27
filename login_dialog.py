# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created: Fri Feb 10 14:35:04 2012
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
        Dialog.resize(388, 158)
        self.emailLine = QtGui.QLineEdit(Dialog)
        self.emailLine.setGeometry(QtCore.QRect(100, 20, 201, 41))
        self.emailLine.setObjectName(_fromUtf8("emailLine"))
        self.pwdLine = QtGui.QLineEdit(Dialog)
        self.pwdLine.setGeometry(QtCore.QRect(100, 70, 201, 41))
        self.pwdLine.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdLine.setObjectName(_fromUtf8("pwdLine"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.loginButton = QtGui.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(260, 120, 101, 31))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "邮箱", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("Dialog", "登陆", None, QtGui.QApplication.UnicodeUTF8))

