#!/usr/bin/python
"""pyCast.py - a python based podcast cli client
    Author: srivathsan (sri@vathsan.com)

Usage:
    pyCast.py add <url> <shortname>
    pyCast.py list
    pyCast.py show <shortname>
    pyCast.py play
    pyCast.py -h | --help
    pyCast.py -v | --version

Options:
    -h --help       Show this message.
    -v --version    Show version.

"""

from docopt import docopt
from podcast import Podcast

if __name__ == "__main__":
    arguments = docopt(__doc__, version="pyCast 0.0.1")
