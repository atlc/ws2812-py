import board
import neopixel
import time

COUNT = 300 # 5 meter strips at 60 leds/meter
BRIGHTNESS = 0.25
FRONT_PIN = board.D18 # physical 12
REAR_PIN = board.D12

ORANGE = (239, 108, 0)
PURPLE = (142, 36, 170)

front = neopixel.NeoPixel(FRONT_PIN, COUNT, brightness=BRIGHTNESS, auto_write=False, pixel_order=(1,0,2,3))
rear = neopixel.NeoPixel(REAR_PIN, COUNT)

def init():
    for x in range(0, COUNT):
        front[x] = (239, 108, 0) if x % 2 == 0 else (142, 36, 170)
    front.show()
    # main()

def main():
    while (1==1):
        time.sleep(3)
        for x in range(0, COUNT):
            front[x] = ORANGE if front[x] == PURPLE else PURPLE


init()