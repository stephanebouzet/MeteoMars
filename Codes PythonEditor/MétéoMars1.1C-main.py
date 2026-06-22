from microbit import *
import music

temp = 0

music.pitch(440)
display.show(Image.YES)
sleep(500)
music.stop()

while True:
    offset = 0
    temp = temperature() + offset

    display.scroll("T=")
    display.scroll(str(temp))

    display.show(Image("""
        99099:
        99900:
        00900:
        00900:
        00099
    """))

    sleep(500)