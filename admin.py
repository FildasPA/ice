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
    track.filepath = "D:/Musique/num/86/Rock/Phrenia - Perspectives.mp3"
    track.duration = 236
    proxy.add(track)

    track.author = "Marty Friedman, Jean-Ken Johnny, KenKen"
    track.title = "The Perfect World"
    track.filepath = "D:/Musique/num/88/Anime/Marty Friedman feat. Jean-Ken Johnny, KenKen _ The Perfect World.mp3"
    track.duration = 236
    proxy.add(track)

    track.author = "Dragon Ball GT"
    track.title = "Dragon Ball GT Opening"
    track.filepath = "D:/Musique/num/88/Anime/Dragon Ball GT Opening.mp3"
    track.duration = 236
    proxy.add(track)

    track.author = "Dragon"
    track.title = ""
    track.filepath = ""
    track.duration = 1

    print("Start stream please!")
    proxy.searchTrackAndStream(track)
    time.sleep(30)
    print("Pause stream please!")
    proxy.pauseStream()
    time.sleep(10)
    print("Resume stream please!")
    proxy.resumeStream()
    time.sleep(30)
    print("Stop stream please!")
    proxy.stopStream()


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
