import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (239, 80, 0)
PURPLE = (95, 0, 95)
GREEN = (15, 15, 100)

color_cycle = 1

def get_color_cycle():
    if (color_cycle % 3 == 0): return ORANGE
    if (color_cycle % 3 == 1): return PURPLE
    if (color_cycle % 3 == 2): return GREEN

for i in range(0, num_pixels):
    if (i % 4 == 0): color_cycle += 1
    pixels[i] = get_color_cycle()

pixels.show()