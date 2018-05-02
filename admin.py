#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import time
import Vocal

#def addTrack(author, title, filepath, duration):
#    track = Vocal.Track()
#
#    track.author = author
#    track.title = title
#    track.filepath = filepath
#    track.duration = int(duration)
#
#    proxy.add(track)


with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
    proxy = Vocal.CollPrx.checkedCast(base)
    if not proxy:
        raise RuntimeError("Invalid proxy")

    #addTrack("Muse",
    #         "Undisclosed Desires",
    #         "D:/Musique/num/86/Rock/Phrenia - Perspectives.mp3",
    #         236)
    #addTrack("Marty Friedman, Jean-Ken Johnny, KenKen",
    #         "The Perfect World",
    #         "D:/Musique/num/88/Anime/Marty Friedman feat. Jean-Ken Johnny, KenKen _ The Perfect World.mp3",
    #         236)
    #addTrack("Dragon Ball GT",
    #         "Dragon Ball GT Opening",
    #         "D:/Musique/num/88/Anime/Dragon Ball GT Opening.mp3",
    #         236)


    track = Vocal.Track()
    track.author = "Dragon"
    track.title = ""
    track.duration = 0
    track.filepath = ""

    print("Start stream please!")
    result = proxy.searchTrackAndStream(track)
    if result == 'none':
        print("No track found...")
    elif result == 'several':
        print("Several tracks found")
    else:
        print("Streaming on %s" %(result))
        time.sleep(600)
        print("Stop!!")
        # time.sleep(30)
        # print("Pause stream please!")
        # proxy.pauseStream()
        # time.sleep(10)
        # print("Resume stream please!")
        # proxy.resumeStream()
        # time.sleep(30)
        # print("Stop stream please!")
        # proxy.stopStream()

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
