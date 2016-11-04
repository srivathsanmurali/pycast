from podcast import Podcast
import yaml
import os

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
