import spidev
import RPi.GPIO as GPIO
import time
from SX127x.LoRa import *
from SX127x.board_config import BOARD

# ADC setup (MCP3008)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 3) << 8) + adc[2]
    return value

# LoRa setup
BOARD.setup()
class LoRaSender(LoRa):
    def _init_(self, verbose=False):
        super(LoRaSender, self)._init_(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0]*6)
    
    def start(self):
        while True:
            soil = read_adc(0)
            temp = read_adc(1)
            payload = f"soil={soil},temp={temp}"

            self.write_payload([ord(c) for c in payload])
            self.set_mode(MODE.TX)
            time.sleep(0.5)
            self.set_mode(MODE.SLEEP)
            print(f"Sent: {payload}")
            time.sleep(10)

lora = LoRaSender(verbose=False)
lora.set_freq(433)
lora.start()
