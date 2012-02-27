from login_dialog import Ui_Dialog
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

from all_feed import login

class LoginDialog(QWidget, Ui_Dialog):
        def __init__(self):
                QWidget.__init__(self)

                self.setupUi(self)

                self.error = QErrorMessage()
                self.error.showMessage('login failed')
                self.error.setVisible(False)
                

                self.loginButton.clicked.connect(self.login_auth)

        @pyqtSlot()
        def login_auth(self):
                email = self.emailLine.text()
                pwd = self.pwdLine.text()

                if email and pwd:
                        try:    
                                login(str(email), str(pwd))
                                print 'login success'
                                self.close()
                                return
                        except:
                                print 'error'
                                self.close()
                                self.error.raise_()
                                self.error.show()
                                return
                else:
                        return



