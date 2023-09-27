import board
import neopixel

pixel_pin = board.D18
num_pixels = 300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, bpp=3, auto_write=False)

pixels.fill((239,108,0,0))
pixels.show()