from microbit import *
import music
from dht20 import DHT20

capteur = DHT20()

# Variables globales
temp = 0
humi = 0

# Initialisation
music.pitch(440, 500)
music.stop()

display.show(Image.YES)


sleep(2000)


def afficher_temperature():
    global temp

    for index in range(2):
        if temp > 20:
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

    sleep(1000)
    display.show(Image.YES)


def afficher_humidite():
    global humi

    for index in range(2):
        if humi > 40 and humi < 80:
            display.scroll("H=")
            display.scroll(str(humi))

            display.show(Image("""
                00900:
                09990:
                99999:
                99999:
                09990
            """))
        else:
            display.show(Image.NO)

    sleep(1000)
    display.show(Image.YES)


while True:
    # Gestion des boutons
    if button_a.was_pressed():
        afficher_temperature()

    if button_b.was_pressed():
        afficher_humidite()

    # Lecture capteur
    temp = capteur.temperature()
    humi = capteur.humidity()

    # Envoi série vers le PC
    print("T = {} °C".format(temp))
    print("H = {} %".format(humi))

    sleep(500)