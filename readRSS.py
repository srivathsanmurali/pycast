#!/usr/bin/python
import feedparser
from pygame import mixer
from subprocess import call, Popen
import sys

def parse(pname):
    d = feedparser.parse(pname)
    print "Read", d.feed.title
    return d

def showEpisodes():
    d = parseSwak()
    eps = range(len(d.entries))
    for i in eps:
        print i, ":", d.entries[i].title
        print "\tNotes:", d.entries[i].description
        print "\n"

def playEpisode():
    if len(sys.argv) < 3:
        printHelp()

    epsNo = 0
    try:
        epsNo = int(sys.argv[2])
    except:
        printHelp()

    d = parseSwak()
    if not len(d.entries[epsNo].enclosures) == 0:
        print epsNo, ":", d.entries[epsNo].title
        playURL(d.entries[epsNo].enclosures[0].url)

def playURL(url):
    #call(["mpg123", url])
    p = Popen(["mpg123","-vC", url])
    p.wait()

def printHelp():
    print "Enter command to process"
    print "./pypass args"
    print "\thelp             -- print this message"
    print "\tshowEps          -- show list of episodes"
    print "\tplayEp epNo      -- plays episode number epNo"
    sys.exit(0)

def parseSwak():
    return parse("http://feeds.feedburner.com/swak")

def main():
    if len(sys.argv) < 2:
        printHelp();
    else:
        cmds = {"help": printHelp,
                "showEps": showEpisodes,
                "playEp": playEpisode}
        userCmd = sys.argv[1]
        if userCmd in cmds:
            cmds[userCmd]()
        else:
            printHelp()


if __name__ == "__main__":
    main()
