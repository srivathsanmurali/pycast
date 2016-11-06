import feedparser
from collections import namedtuple
import yaml
import os
import urllib

""" Episode - stores information about each episode"""
Episode = namedtuple ("Episode", "title, notes, url, pubDate, played, \
                    curPosition, downloaded")

class Podcast:
    """ Podcast - a simple class that represents the data for each podcast
    """
    def __init__(self, _url, root, shortname):
        self.shortname      = shortname
        self.url            = _url
        self.numEpisodes    = 0
        self.episodes       = dict()
        self.podcastDir     = os.path.join(root, shortname)
        self.podcastFile    = os.path.join(self.podcastDir, 'podcast.yml')
        if not os.path.exists(self.podcastFile):
            self.dump()

    def dump (self):
        if not os.path.exists(self.podcastDir):
          os.makedirs(self.podcastDir)

        with open(self.podcastFile, 'w') as outfile:
          yaml.dump({'shortname'    : self.shortname,
                     'url'          : self.url,
                     'numEpisodes'  : self.numEpisodes,
                     'episodes'     : self.episodes,
                     'podcastDir'   : self.podcastDir,
                     'podcastFile'  : self.podcastFile,
                    }, outfile, default_flow_style=True)

    def load (self):
        if os.path.exists(self.podcastFile):
          with open(self.podcastFile, 'r') as infile:
            config = yaml.load(infile)
            self.shortname      = config['shortname']
            self.url            = config['url']
            self.numEpisodes    = config['numEpisodes']
            self.episodes       = config['episodes']
            self.podcastDir     = config['podcastDir']
            self.podcastFile    = config['podcastFile']

    #def delete (self):
    def updateFeed(self):
        self.load()
        try:
            podFeed = feedparser.parse(self.url)
        except:
            return False

        if len(podFeed.entries) == 0:
            print "No episodes yet"
        else:
            for epId, eps in enumerate(reversed(podFeed.entries)):
                """ also check if the enclosure
                    contains a mp3 url"""
                if len(eps.enclosures) >0 and epId not in self.episodes:
                    self.episodes[epId] = Episode(eps.title, eps.description, eps.enclosures[0].url, eps.updated_parsed, False, 0.0, True)
                    self.numEpisodes = self.numEpisodes + 1
        self.dump()
        return True

    def showEpisodes(self):
        self.load()
        for i in self.episodes:
            print '{}:'.format(i), self.episodes[i].title

    def getEpisodeDetails(self, epId):
        self.load()
        if epId < 0 or epId > self.numEpisodes:
            return 0;
        else:
            return self.episodes[epId]

    def getLastEpisode(self):
        self.load()
        if self.numEpisodes == 0:
            return 0
        else:
            return self.episodes[0]

    def getEpisodes(self):
        self.load()
        if self.numEpisodes == 0:
            return 0
        else:
            return self.episodes

    def download(self, epId):
        epName = os.path.join(self.podcastDir, ''.join([str(epId), '.mp3']))
        if os.path.exists (epName):
            print '{} already downloaded.'.format(epName)
        else:
            self.load()
            ep = self.episodes[epId]
            ep.downloaded = True
            urllib.urlretrieve(ep.url, epName)
            print '{} downloaded.'.format(epName)

def main():
    swak = Podcast("http://feeds.feedburner.com/swak", '.', 'swak')
    swak.updateFeed()
    swak.showEpisodes()
    print swak.getLastEpisode()

if __name__ == "__main__":
    main()
