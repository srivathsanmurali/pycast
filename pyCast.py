#!/usr/bin/python
"""pyCast.py - a python based podcast cli client
    Author: srivathsan (sri@vathsan.com)

Usage:
    pyCast.py podcast add <url>
    pyCast.py podcast list
    pyCast.py podcast show <name>
    pyCast.py podcast play
    pyCast.py -h | --help
    pyCast.py -v | --version

Options:
    -h --help       Show this message.
    -v --version    Show version.

"""

from docopt import docopt
from core import podcast

if __name__ == "__main__":
    arguments = docopt(__doc__, version="pyCast 0.0.1")

    if arguments['podcast'] and arguments['add']:
        print "podcast add", arguments['<url>']
