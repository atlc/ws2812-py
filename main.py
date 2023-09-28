import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 600
zero = 70

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.75,
                           bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (160, 20, 0)
PURPLE = (20, 0, 20)
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
    for i in range(zero, num_pixels):
        pixels[i] = ORANGE if i < num_pixels / 2 else PURPLE
    pixels.show()

    is_purple = False
    offset = zero
    run_count = 0

    while (offset < num_pixels):
        pixels[offset] = ORANGE if is_purple else PURPLE
        pixels.show()
        offset += 1
        time.sleep(0.005)
        if (offset+1 >= num_pixels):
            run_count += 1
            offset = zero
            is_purple = not is_purple


moving_dual_color()
