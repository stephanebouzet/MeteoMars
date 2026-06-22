from microbit import *
import music

temp = 0
offset = -4

# Initialisation
music.pitch(440, 100)
music.stop()

display.show(Image.YES)

uart.init(115200)

sleep(2000)

while True:
    temp = temperature() + offset

    # Envoi vers le PC par USB série
    uart.write("T={}C\r\n".format(temp))

    if temp > 20:
        display.scroll("T=", wait=False)
        sleep(500)
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

    sleep(500)