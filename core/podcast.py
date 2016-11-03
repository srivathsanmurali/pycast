import feedparser
from collections import namedtuple

""" Episode - stores information about each episode"""
Episode = namedtuple ("Episode", "title, notes, url, pubDate, played, curPosition")

class Podcast:
    """ Podcast - a simple class that represents the data for each podcast
    """
    def __init__(self, _url):
        self.url            = _url
        self.numEpisodes    = 0
        self.episodes       = dict()
        self.updateFeed()

    def updateFeed(self):
            podFeed = feedparser.parse(self.url)
            print 'Read "', podFeed.feed.title, '"'
            if len(podFeed.entries) == 0:
                print "No episodes yet"
            else:
                for eps in podFeed.entries:
                    """ also check if the enclosure
                        contains a mp3 url"""
                    if len(eps.enclosures) >0:
                        self.episodes[self.numEpisodes] = Episode(eps.title, eps.description, eps.enclosures[0].url, eps.updated_parsed, False, 0.0)
                        self.numEpisodes = self.numEpisodes + 1
            self.pubDate = podFeed.feed.updated_parsed

    def showEpisodes(self):
        for i in list(self.episodes.values()):
            print i.title

    def getEpisodeDetails(self, epId):
        if epId < 0 or epId > self.numEpisodes:
            return 0;
        else:
            return self.episodes[epId]

    def getLastEpisode(self):
        if self.numEpisodes == 0:
            return 0
        else:
            return self.episodes[0]

    def getEpisodes(self):
        if self.numEpisodes == 0:
            return 0
        else:
            return self.episodes

    """ def updateFeed(self): """

def main():
    swak = Podcast("http://feeds.feedburner.com/swak")

if __name__ == "__main__":
    main()
