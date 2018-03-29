import vlc
import time
import socket

filepath = '/home/etudiants/inf/uapv1502198/s2/muse.mp3'

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(filepath)

ip = socket.gethostbyname(socket.gethostname())
port = 8080
print("Will stream on: "+str(ip)+":"+str(port))
print("--------------------------------------------------------")
options = ':sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{mux=mp3,dst=:%s/}' %(str(port))
media = instance.media_new(filepath, options)
player.set_media(media)
player.play()

time.sleep(5)

print(media)
player.set_media(None)
media = None
print(media)

#time.sleep(236)
