#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import socket
import time
import Vocal

filepath = '/home/etudiants/inf/uapv1502198/s2/muse.mp3'


port = 8080

ip = socket.gethostbyname(socket.gethostname())
print("Will stream on: "+str(ip)+":"+str(port))
print("--------------------------------------------------------")
media = instance.media_new(filepath)
options = ':sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{mux=mp3,dst=:%s/}' %(str(port))
media = instance.media_new(filepath, options)
player.set_media(media)
player.play()

time.sleep(236)

class CollI(Vocal.Coll):

    def __init__(self):
        self.collection = []
        self.instance = vlc.Instance()
        self.player = instance.media_player_new()
        self.media = None

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
        #ip = socket.gethostbyname(socket.gethostname())
        #print("Will stream on: "+str(ip)+":"+str(port))
        #print("--------------------------------------------------------")
        if self.media not None:
            self.player.set_media(None)
            self.media = None

        media = instance.media_new(track.filepath)
        options = ':sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{mux=mp3,dst=:%s/}' %(str(port))
        media = instance.media_new(filepath, options)
        player.set_media(media)
        player.play()

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
