#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import time
import Vocal

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
    proxy = Vocal.CollPrx.checkedCast(base)
    if not proxy:
        raise RuntimeError("Invalid proxy")

    track = Vocal.Track()

    track.author = "Muse"
    track.title = "Undisclosed Desires"
    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse.mp3"
    track.duration = 236
    proxy.add(track)

    track.author = "Muse"
    track.title = ""
    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse2.mp3"
    track.duration = 236
    proxy.add(track)

    track.author = "Muse"
    track.title = ""
    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse3.mp3"
    track.duration = 236
    proxy.add(track)



def playTrack():
    print(i)


#status = 0
#ic = None
#try:
#    ic = Ice.initialize(sys.argv)
#    base = ic.stringToProxy("Coll:default -p 10000")
#    coll = Vocal.CollPrx.checkedCast(base)
#    if not coll:
#        raise RuntimeError("Invalid proxy")
#
#    track = Vocal.Track()
#
#    track.author = "Muse"
#    track.title = "Undisclosed Desires"
#    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse.mp3"
#    track.duration = 236
#    proxy.add(track)
#
#    track.author = "Muse"
#    track.title = ""
#    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse2.mp3"
#    track.duration = 236
#    proxy.add(track)
#
#    track.author = "Muse"
#    track.title = ""
#    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse3.mp3"
#    track.duration = 236
#    proxy.add(track)
#
#except:
#    traceback.print_exc()
#    status = 1
#
#if ic:
#    # Clean up
#    try:
#        ic.destroy()
#    except:
#        traceback.print_exc()
#        status = 1
#
#sys.exit(status)
