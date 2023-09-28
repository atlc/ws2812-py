import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1,
                           bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (239, 80, 0)
PURPLE = (95, 0, 95)
GREEN = (15, 100, 15)


def static_tricolor():
    color_cycle = 1

    def get_color_cycle():
        if (color_cycle % 3 == 0):
            return ORANGE
        if (color_cycle % 3 == 1):
            return PURPLE
        if (color_cycle % 3 == 2):
            return GREEN

    for i in range(0, num_pixels):
        if (i % 4 == 0):
            color_cycle += 1
        pixels[i] = get_color_cycle()

    pixels.show()


def moving_dual_color():
    for i in range(0, num_pixels):
        pixels[i] = ORANGE if i < num_pixels / 2 else PURPLE
    pixels.show()

    is_purple = False
    offset = 0

    while (offset < num_pixels):
        print(offset)
        pixels[offset] = ORANGE if is_purple else PURPLE
        pixels.show()
        offset += 1
        time.sleep(0.05)
        if (offset+1 >= num_pixels):
            print('\n\n\n\n\RESET HIT\n\n\n\n')
            offset = 0
            is_purple = not is_purple


moving_dual_color()