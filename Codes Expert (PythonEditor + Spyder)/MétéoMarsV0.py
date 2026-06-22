import serial
import csv
import time
import matplotlib.pyplot as plt

PORT = "COM6"       # à adapter
VITESSE = 115200
FICHIER = "mesures_dht20.csv"

ser = serial.Serial(PORT, VITESSE, timeout=1)

temperatures = []
humidites = []
n_mesure = 10

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

while True:
    ligne = ser.readline().decode("utf-8").strip()

    if ligne:
        print(ligne)

    try:
        temp, humi = ligne.split(";")
        temp = float(temp)
        humi = float(humi)

        temperatures.append(temp)
        humidites.append(humi)

        with open(FICHIER, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([temp, humi])

        if len(temperatures) % n_mesure == 0:
            ax1.clear()
            ax1.plot(temperatures)
            ax1.set_title("Température")
            ax1.set_ylabel("°C")
            ax1.grid()

            ax2.clear()
            ax2.plot(humidites)
            ax2.set_title("Humidité")
            ax2.set_xlabel("Mesures")
            ax2.set_ylabel("%")
            ax2.grid()

            plt.tight_layout()
            plt.pause(0.1)

    except :
        pass
