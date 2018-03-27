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

    track.author = "auteur"
    track.title = "titre"
    track.filepath = "filepath"
    track.duration = 0

    coll.add(track)

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

