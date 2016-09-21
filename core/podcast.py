#!/usr/bin/python
import feedparser

class Podcast:
    """ Podcast - a simple class that represents the data for each podcast
    """
    def __init__(self, _url):
        self.url        = _url
        self.podFeed    = feedparser.parse(self.url)
        print "Read", self.podFeed.feed.title

    def showEpisodes(self):
        eps = self.podFeed.entries
        for i in eps:
            print i.title
            # print "\tNotes:", self.podFeed.entries[i].description
            # print "\n"
def main():
    swak = Podcast("http://feeds.feedburner.com/swak")
    swak.showEpisodes()

if __name__ == "__main__":
    main()
