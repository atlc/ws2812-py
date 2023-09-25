import board
import neopixel
import time

COUNT = 300 # 5 meter strips at 60 leds/meter
FRONT_PIN = board.D5 # GPIO pin 5, physical pin 29
REAR_PIN = board.D6 # GPIO pin 6, physical pin 31

ORANGE = (239, 108, 0)
PURPLE = (142, 36, 170)

front = neopixel.NeoPixel(FRONT_PIN, COUNT)
rear = neopixel.NeoPixel(REAR_PIN, COUNT)

def init():
    for x in range(0, COUNT):
        front[x] = ORANGE if x % 2 == 0 else PURPLE
    main()

def main():
    while (1==1):
        time.sleep(3)
        for x in range(0, COUNT):
            front[x] = ORANGE if front[x] == PURPLE else PURPLE

        
init()