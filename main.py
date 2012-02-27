from main_window import Ui_MainWindow
from login_dialog import Ui_Dialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login import LoginDialog
from feed_dialog import FeedDialog
from content_dialog import ContentDialog
from core import *
import feedparser
import shelve

class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self):
                QMainWindow.__init__(self)

                self.setupUi(self)

                self.has_login = False

                self.login_dialog = LoginDialog()
                self.login_dialog.setVisible(False) 

                self.feed_dialog = FeedDialog()
                self.feed_dialog.setVisible(False)

                self.content_dialog = ContentDialog()
                self.content_dialog.setVisible(False)

                self.loginAction.triggered.connect(self.login)
                self.subAction.triggered.connect(self.sub)

                self.sourceLIst.clicked.connect(self.get_a_rss_list)
                self.contentList.clicked.connect(self.get_a_rss_content)

                if self.if_has_login():
                        self.show_all_rss()

        def if_has_login(self):
                auth_file = shelve.open('auth')
                sid_file = shelve.open('sid')

                if 'auth' in auth_file.keys() and 'sid' in sid_file.keys():
                        self.has_login = True
                        return True
                return False

        @pyqtSlot()
        def login(self):
                self.login_dialog.setVisible(True)
                self.login_dialog.setFocus()
                self.login_dialog.raise_()
                self.login_dialog.show()

                self.has_login = True

                self.show_all_rss()

        @pyqtSlot()
        def sub(self):
                self.feed_dialog.setVisible(True)
                self.feed_dialog.setFocus()
                self.feed_dialog.raise_()
                self.feed_dialog.show()

        @pyqtSlot('QModelIndex')
        def get_a_rss_list(self, model_index):
                if self.has_login and self.feed_data:
                        feed = self.feed_data.get_a_feed_by_index(model_index.row())

                        if feed:
                                self.this_site_feed = ASiteFeed(feed)
                                content_list = self.this_site_feed.list_all_title()
                                content_list_model = QStringListModel()
                                content_list_model.setStringList(content_list)
                                self.contentList.setModel(content_list_model)


        @pyqtSlot('QModelIndex')
        def get_a_rss_content(self, model_index):
                if self.has_login and self.this_site_feed:
                        article = self.this_site_feed.list_article_by_index(model_index.row())
                        html = article['summary']
                        rss = article['link']

                        self.content_dialog.set_html(html)
                        self.content_dialog.set_site(rss)
                        
                        self.content_dialog.setVisible(True)
                        self.content_dialog.raise_()
                        self.content_dialog.show()


        def show_all_rss(self):
                if self.has_login:
                       self.feed_data = FeedData()
                       rss_list = QStringList(self.feed_data.list_all_name())
                       rss_list_model = QStringListModel()
                       rss_list_model.setStringList(rss_list)
                       self.sourceLIst.setModel(rss_list_model)
                       


if __name__ == '__main__':
        import sys
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())
        
