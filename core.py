import feedparser
import webbrowser
from all_feed import get_all_feed

ATOM = "http://www.google.com/reader/atom/feed/"

"""
    This class assume the user has login
"""
class FeedData(object):
    def __init__(self):
        #self.email = email
        #self.password = password
       
        self.feeds = get_all_feed()

    def list_all_name(self):

        if self.feeds:
            name_list = self.feeds.keys()

        return name_list

    def list_all_website(self):

        if self.feeds:
            website_list = self.feeds.values()

        return website_list

    def get_a_feed(self, title):
        if self.feeds and title in self.feeds:
            feed = feedparser.parse(self.feeds[title])
            return feed
        
        return None

    def get_a_feed_by_index(self, index):
        if self.feeds:
            if index < len(self.feeds.values()):
                feed = feedparser.parse(self.feeds.values()[index])
                return feed
        return None


class ASiteFeed(object):
    def __init__(self, feed):
        self.feed = feed

        items = self.feed['items']

        self.data = []

        for item in items:
            self.data.append({'title' : item.title,
                         'summary' : item.summary,
                         'link' : item.link})

    def list_all_title(self):
        all_title = []

        for d in self.data:
            all_title.append(d["title"])

        return all_title

    def list_article_by_title(self, t):
        article = {}

        for arti in self.data:
            if arti['title'] == t:
                aritcle = arit
                break
            
        if not article:
            return None

        summary = article['summary']
        title = article['title']
        link = article['link']

        return article

    def list_article_by_index(self, index):
        if index < len(self.data):
            article = self.data[index]
            return article
        
        return None

    def open_article_by_title(self, title):

        for article in self.data:
            if title == article['title']:
                link = article['link']
                webbrowser.open(link)
                return

        return

    def open_article_by_index(self, index):
        if index < len(self.data):
            link = self.data[index]['link']

            webbrowser.open(link)
            return
        return


if __name__ == '__main__':

    email = raw_input("Email: ")
    password = raw_input("Password: ")
    
    feed_data = FeedData(email, password)

    print feed_data.list_all_name(), '\n'

    print feed_data.list_all_website()

    feeds = ASiteFeed(feed_data.get_a_feed_by_index(0))

    all_title = feeds.list_all_title()

    for i in all_title:
        print i, '\n'

    feeds.open_article_by_index(0)

    input('end')
    

    
