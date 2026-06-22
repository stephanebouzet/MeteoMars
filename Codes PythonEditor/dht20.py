from microbit import *
import utime

class DHT20:

    def __init__(self):
        self.addr = 0x38

        # Initialisation du capteur
        try:
            i2c.write(self.addr, b'\x71')
        except:
            pass

        sleep(100)

    def _read_raw(self):

        # Déclenche une mesure
        i2c.write(self.addr, b'\xAC\x33\x00')

        sleep(80)

        # Attente fin mesure
        while True:
            data = i2c.read(self.addr, 7)
            if (data[0] & 0x80) == 0:
                break
            sleep(10)

        return data

    def temperature(self):

        data = self._read_raw()

        raw_temp = ((data[3] & 0x0F) << 16) | \
                   (data[4] << 8) | \
                    data[5]

        temp = (raw_temp * 200.0 / 1048576.0) - 50.0

        return round(temp, 1)

    def humidity(self):

        data = self._read_raw()

        raw_humi = (data[1] << 12) | \
                   (data[2] << 4) | \
                   (data[3] >> 4)

        humi = raw_humi * 100.0 / 1048576.0

        return round(humi, 1)