#!/usr/bin/python
"""pyCast.py - a python based podcast cli client
    Author: srivathsan (sri@vathsan.com)

Usage:
    pyCast add <url> <shortname>
    pyCast remove <shortname>
    pyCast list
    pyCast show <shortname>
    pyCast play <shortname> <epId>
    pyCast update
    pyCast -h | --help
    pyCast -v | --version

Options:
    -h --help       Show this message.
    -v --version    Show version.

"""

from docopt import docopt
from podcastManager import PodcastManager

if __name__ == "__main__":
    args = docopt(__doc__, version="pyCast 0.0.1")
    pm = PodcastManager()
    if args['add'] and args['<shortname>'] and args['<url>']:
        pm.add(str(args['<url>']), str(args['<shortname>']))
    elif args['remove'] and args['<shortname>']:
        pm.remove(str(args['<shortname>']))
    elif args['list']:
        pm.list()
    elif args['update']:
        pm.update()
    elif args['show'] and args['<shortname>']:
        pm.show(str(args['<shortname>']))
