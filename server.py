#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import socket
import time
import Vocal

class Player:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = None
        print("Initialized player!")

    def start(self, filepath, duration, ip, port):
        self.stop()

        options = ':sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{mux=mp3,dst=:%s/}' %(str(port))
        self.media = self.instance.media_new(filepath, options)
        self.player.set_media(self.media)
        self.player.play()

    def pause(self):
        if self.media != None:
            self.player.pause()

    def resume(self):
        if self.media != None:
            self.player.pause()

    def stop(self):
        if self.media != None:
            self.player.stop()
            self.player.set_media(None)
            self.media = None


class CollI(Vocal.Coll):

    def __init__(self):
        self.collection = []
        self.player = Player()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 8181
        print("Initialized!")

    def add(self, track, current=None):
        print("Add track: " + track.title)
        self.collection.append(track)

    def search(self, track, current=None):
        print("Search track")
        c = []
        for t in self.collection:
            if (track.author and track.author in t.author) or (track.title and track.title in t.title):
                c.append(t)
        return c

    # Get a track object with possibly incomplete informations
    # Search for track(s) in the server collection
    # If no track was found, it returns "none"
    # If exactly one track is found, it returns a stream address
    # If several tracks are found, it returns "several"
    def searchTrackAndStream(self, track, current=None):
        c = self.search(track)
        print(str(c))
        if not c:
            return ""
        elif len(c) == 1:
            self.startStream(c[0])
        else:
            return "several"

    def startStream(self, track, current=None):
        dst = str(self.ip)+":"+str(self.port)
        self.player.start(track.filepath, track.duration, self.ip, self.port)
        print("streaming %s on %s" %(track.filepath, dst))
        return dst

    def pauseStream(self, current=None):
        print("Pause Stream!")
        self.player.pause()

    def resumeStream(self, current=None):
        print("Resume Stream!")
        self.player.resume()

    def stopStream(self, current=None):
        print("Stop Stream!")
        self.player.stop()


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
    object = CollI()
    adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
    adapter.activate()
    communicator.waitForShutdown()

#status = 0
#ic = None
#try:
#    ic = Ice.initialize(sys.argv)
#    adapter = ic.createObjectAdapterWithEndpoints("CollAdapter", "default -p 10000")
#    object = CollI()
#    adapter.add(object, ic.stringToIdentity("Coll"))
#    adapter.activate()
#    ic.waitForShutdown()
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
