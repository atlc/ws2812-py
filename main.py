import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (239, 80, 0)
PURPLE = (142, 0, 170)

is_orange = True

for i in range(0, num_pixels):
    if (i % 6 == 0): is_orange = not is_orange
    pixels[i] = ORANGE if is_orange else PURPLE

pixels.show()