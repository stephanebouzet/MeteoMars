from microbit import *
import music

temp = 0

# Bip de démarrage
music.pitch(440)
sleep(300)
music.stop()

display.show(Image.YES)
sleep(2000)

while True:
    offset = 0
    temp = temperature() + offset

    if temp > 20:
        music.stop()

        display.scroll("T=")
        display.scroll(str(temp))

        display.show(Image("""
            99099:
            99900:
            00900:
            00900:
            00099
        """))

    else:
        display.show(Image.NO)
        music.pitch(262)

    sleep(500)