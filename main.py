import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (239, 108, 0)
PURPLE = (142, 36, 170)

for i in range(0,num_pixels):
    pixels[i] = ORANGE if i % 2 == 0 else PURPLE

pixels.show()