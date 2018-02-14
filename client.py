import sys, Ice
import vlc
import time
import TP

#with Ice.initialize(sys.argv) as communicator:
#    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
#    printer = Demo.PrinterPrx.checkedCast(base)
#    if not printer:
#        raise RuntimeError("Invalid proxy")
#
#    printer.printString("Hello World!")

communicator = Ice.initialize(sys.argv)
base = communicator.stringToProxy("SimplePrinter:default -p 10000")
server = TP.CollPrx.checkedCast(base)
if not server:
    raise RuntimeError("Invalid proxy")

#server.printString("Hello World!")
track = server.getTrack();
#
instance = vlc.Instance()
#
#Create a MediaPlayer with the default instance
player = instance.media_player_new()
#
#Load the media file
media = instance.media_new(track.filePath)
#
#Add the media to the player
player.set_media(media)
#
#Play for 10 seconds then exit
player.play()
time.sleep(track.length)
