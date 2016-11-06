from podcast import Podcast
import yaml
import os
import shutil

class PodcastManager:
  """
  PodcastManager - manages our list of podcasts
  Members:
    - downloadLimit = 5
    - listOfPodcasts = {shortname:url}
  """
  def __init__(self, _rootDir = os.path.expanduser('~/.pyCast/')):
    self.rootDir        = _rootDir
    self.configFile     = os.path.join(self.rootDir, 'config.yml')
    self.downloadLimit  = 5
    self.listOfPodcasts = {}
    if not os.path.exists(self.rootDir):
        os.makedirs(self.rootDir)
        self.dump()

  def dump(self):
    if not os.path.exists(self.rootDir):
      os.makedirs(self.rootDir)

    with open(self.configFile, 'w') as outfile:
      yaml.dump({'downloadLimit' : self.downloadLimit,
        'rootDir'       : self.rootDir,
        'listOfPodcasts': self.listOfPodcasts}, outfile, default_flow_style=True)

  def load(self):
    if os.path.exists(self.configFile):
      with open(self.configFile, 'r') as infile:
        config = yaml.load(infile)
        self.downloadLimit = config['downloadLimit']
        self.listOfPodcasts = config['listOfPodcasts']

  def add(self, url, shortname):
    self.load()
    if shortname in self.listOfPodcasts:
      print '"{}" already in list of podcasts'.format(shortname)
      print 'check pyCast show "{}"'.format(shortname)
    else:
      """
      1) check for validity of feed
      2) save to dist
      3) run podcast Update
      """
      newPodcast = Podcast(url, self.rootDir, shortname)
      if newPodcast.updateFeed():
        self.listOfPodcasts[shortname] = url
        print "{}:{} added to list of podcasts".format(shortname, url)
        self.dump()
      else:
        del newPodcast
        print "{}:{} cound not be added.".format(shortname, url)

  def remove(self, shortname):
    self.load()
    if not shortname in self.listOfPodcasts:
      print '"{}" not in list of podcasts'.format(shortname)
    else:
      del self.listOfPodcasts[shortname]
      p = Podcast('',self.rootDir, shortname)
      shutil.rmtree(p.podcastDir)
      print '"{}" removed from list of podcasts'.format(shortname)
      self.dump()

  def list(self):
    self.load()
    for i in self.listOfPodcasts:
      print i, ":", self.listOfPodcasts[i]

  def update(self):
    self.load()
    for i in self.listOfPodcasts:
      print 'updating "{}".'.format(i)
      p = Podcast('', self.rootDir, i)
      p.updateFeed()

  def show(self, shortname):
    self.load()
    if shortname not in self.listOfPodcasts:
      print '"{}" not in list of podcasts'.format(shortname)
    else:
      p = Podcast('', self.rootDir, shortname)
      p.showEpisodes()

  def download(self, shortname, epId):
    self.load()
    if shortname not in self.listOfPodcasts:
      print '"{}" not in list of podcasts'.format(shortname)
    else:
      p = Podcast('', self.rootDir, shortname)
      p.download(epId)



