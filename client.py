#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import time
import Vocal


status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("Coll:default -p 10000")
    coll = Vocal.CollPrx.checkedCast(base)
    if not coll:
        raise RuntimeError("Invalid proxy")

    track = Vocal.Track()

    track.author = "Muse"
    track.title = "Undisclosed Desires"
    track.filepath = "/home/etudiants/inf/uapv1502198/s2/muse.mp3"
    track.duration = 236

    coll.add(track)

    track2 = Vocal.Track()

    track.author = "us"

    c = coll.search(track2)

    for t in c:
        print "- " + t.title

except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)





#track = server.getTrack();
#instance = vlc.Instance()
#player = instance.media_player_new()
#media = instance.media_new(track.filePath)
#player.set_media(media)
#player.play()
#
#while 1:
#	a = raw_input()
#	if a == "pause":
#		player.pause()
#	elif a == "stop":
#		player.stop()
#		break

#time.sleep(track.length)

