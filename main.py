import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (108, 239, 0) # In GRB
PURPLE = (36, 142, 170) # In GRB

for i in range(0,num_pixels):
    pixels[i] = ORANGE if i % 2 == 0 else PURPLE

pixels.show()