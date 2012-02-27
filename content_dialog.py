from PyQt4.QtCore import *
from PyQt4.QtGui import *
from rss_content import Ui_Dialog
import webbrowser

class ContentDialog(QWidget, Ui_Dialog):
        def __init__(self):
                QWidget.__init__(self)

                self.setupUi(self)

                self.site = None

                self.pushButton.clicked.connect(self.see_original)

        def set_html(self, html):
                self.rssContentView.setHtml(html)

        def set_site(self, rss_site):
                self.site = rss_site

        def see_original(self, ss):
                if self.site:
                        webbrowser.open(self.site)
        
        @classmethod
        def show_content(cls, html_content, rss_site):

                content = ContentDialog(html_content, rss_site)

                content.raise_()
                content.setVisible(True)
                content.show()

