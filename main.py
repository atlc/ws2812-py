import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, bpp=3, auto_write=False, pixel_order=neopixel.GRBW)

pixels.fill((239,108,0))
pixels.show()