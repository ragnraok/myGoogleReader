from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from rss_feed_dialog import Ui_rssFeedDialog
from all_feed import sub_a_feed

class FeedDialog(QWidget, Ui_rssFeedDialog):
        def __init__(self):
                QWidget.__init__(self)

                self.setupUi(self)

                self.error = QErrorMessage()
                self.error.setVisible(False)

                self.pushButton.clicked.connect(self.sub_feed)


        @pyqtSlot()
        def sub_feed(self):
            address = self.lineEdit.text()

            r = sub_a_feed(address)

            self.close()
            if r:
                    self.error.showMessage('success')
            else:
                    self.error.showMessage('failed')

            self.error.setVisible(True)
            self.error.raise_()
            self.error.show()
