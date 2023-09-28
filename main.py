import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, bpp=3, auto_write=True, pixel_order=neopixel.GRB)

ORANGE = (239, 80, 0)
PURPLE = (142, 0, 170)

for i in range(1, 100):
    for j in range(1, 3):
        pixels[i*j] = ORANGE if i % 2 == 0 else PURPLE