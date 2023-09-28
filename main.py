import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (239, 80, 0)
PURPLE = (142, 0, 170)

i = 0
while (i<=num_pixels):
    pixels[i] = ORANGE if i % 2 == 0 else PURPLE
    pixels[i+1] = ORANGE if i % 2 == 0 else PURPLE
    pixels[i+2] = ORANGE if i % 2 == 0 else PURPLE
    if (i+3 <= num_pixels):
        i+=3

pixels.show()