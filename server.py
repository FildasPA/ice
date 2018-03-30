#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import socket
import time
import Vocal

filepath = '/home/etudiants/inf/uapv1502198/s2/muse.mp3'

class CollI(Vocal.Coll):

    def __init__(self):
        self.collection = []
        self.instance = vlc.Instance()
        self.player = instance.media_player_new()
        self.media = None
        self.port = 8080

    def add(self, track, current=None):
        print "Add track: " + track.title
        self.collection.append(track)

    def search(self, track, current=None):
        print "Search track"
        c = []

        for t in self.collection:
            if (track.author in t.author) or (track.title in t.title):
                c.append(t)

        return c

    def streamTrack(self, track, current=None):
        if self.media not None:
            self.player.set_media(None)
            self.media = None

        options = ':sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{mux=mp3,dst=:%s/}' %(str(self.port))
        self.media = instance.media_new(track.filepath, options)
        self.player.set_media(media)
        self.player.play()

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("CollAdapter", "default -p 10000")
    object = CollI()
    adapter.add(object, ic.stringToIdentity("Coll"))
    adapter.activate()
    ic.waitForShutdown()
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
