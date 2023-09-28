import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 600
zero = 180  # 0 to show all of the strips, 70 to truncate wall lights, 180 to truncate wall and west side
offset = zero  # used for cancelling movable events

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.75,
                           bpp=3, auto_write=False, pixel_order=neopixel.GRB)

ORANGE = (160, 20, 0)
PURPLE = (20, 0, 40)
GREEN = (15, 100, 15)


def constant_dual_color():
    off()
    color_cycle = 1

    for i in range(0, num_pixels):
        pixels[i] = ORANGE if color_cycle % 3 == 0 else PURPLE
        if (i % 4 == 0):
            color_cycle += 1

    pixels.show()


def constant_tri_color():
    off()
    color_cycle = 1

    def get_color_cycle():
        if (color_cycle % 3 == 0):
            return ORANGE
        if (color_cycle % 3 == 1):
            return PURPLE
        if (color_cycle % 3 == 2):
            return GREEN

    for i in range(0, num_pixels):
        pixels[i] = get_color_cycle()
        if (i % 4 == 0):
            color_cycle += 1

    pixels.show()


def moving_dual_color():
    off()
    for i in range(zero, num_pixels):
        pixels[i] = ORANGE if i < num_pixels / 2 else PURPLE
    pixels.show()

    is_purple = False
    run_count = 0
    offset = zero  # reassigning it here so that subsequent invocations after turning off can operate

    while (offset < num_pixels):
        pixels[offset] = ORANGE if is_purple else PURPLE
        pixels.show()
        offset += 1
        time.sleep(0.005)
        if (offset+1 >= num_pixels):
            run_count += 1
            offset = zero
            is_purple = not is_purple


def off():
    offset = num_pixels+1  # used to cancel otherwise infinite while loop
    for i in range(0, num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.show()
