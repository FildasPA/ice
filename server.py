#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, traceback, Ice
import vlc
import socket
import time
import Vocal

ip = socket.gethostbyname(socket.gethostname())
port = 5005

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
        self.addTracks()
        print("Initialized!")

    def add(self, track, current=None):
        print("Add track: " + track.title)
        self.collection.append(track)

    def addTrack(self, author, title, filepath, duration):
        track = Vocal.Track()

        track.author = author
        track.title = title
        track.filepath = filepath
        track.duration = int(duration)

        self.add(track)

    def search(self, track, current=None):
        print("Search track: title: '%s', author: '%s'" %(track.title, track.author))
        c = []
        for t in self.collection:
            if (track.author and track.author.lower() in t.author.lower()) \
                or (track.title and track.title.lower() in t.title.lower()):
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
            print("No track found...")
            return "none"
        elif len(c) == 1:
            print("Streaming!")
            return self.startStream(c[0])
        else:
            print("Several tracks found")
            return "several"

    def startStream(self, track, current=None):
        dst = str(self.ip)+":"+str(self.port)
        self.player.start(track.filepath, track.duration, self.ip, self.port)
        print("Streaming '%s' on %s" %(track.filepath, dst))
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

    def addTracks(self):
        self.addTrack("Muse",
             "Undisclosed Desires",
             "D:/Musique/num/86/Rock/Phrenia - Perspectives.mp3",
             236)
        self.addTrack("Marty Friedman, Jean-Ken Johnny, KenKen",
             "The Perfect World",
             "D:/Musique/num/88/Anime/Marty Friedman feat. Jean-Ken Johnny, KenKen _ The Perfect World.mp3",
             236)
        self.addTrack("Dragon Ball GT",
             "Dragon Ball GT Opening",
             "D:/Musique/num/88/Anime/Dragon Ball GT Opening.mp3",
             236)


with Ice.initialize(sys.argv) as communicator:
    address = "tcp -h %s -p %s" %(ip, port)
    print("IceServer address: %s" %(address))
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", address)
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
