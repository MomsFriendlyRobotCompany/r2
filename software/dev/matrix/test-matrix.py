#!/usr/bin/env python
# Note: you have to use a modified version of the Adafruit library because
# PIL/Pillow suck!!
import time

#from PIL import Image
#from PIL import ImageDraw
import numpy as np
from Adafruit_LED_Backpack_kw import Matrix8x8

class MatrixArray(object):
    def __init__(self, ids):
        self.lcds = []
        for id in ids:
            self.lcds.append(Matrix8x8.Matrix8x8(address=id))

        for lcd in self.lcds:
            lcd.begin()
            lcd.clear()
            lcd.write_display()

    def __del__(self):
        for lcd in self.lcds:
            lcd.clear()
            lcd.write_display()

    def random(self, lcds=None):
        for lcd in self.lcds:
            pts = np.random.randint(2, size=64)
            lcd.clear()
            for i, v in enumerate(pts):
              lcd.set_pixel(i//8, i%8, v)
            lcd.write_display()

m = MatrixArray([0x70, 0x72, 0x73])

for _ in range(50):
    m.random()
    time.sleep(0.1)

# Create display instance on default I2C address (0x70) and bus number.
# display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# On BeagleBone, try busnum=2 if IOError occurs with busnum=1
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=2)

# Initialize the display. Must be called once before using the display.
# display.begin()

# pts = np.random.randint(2, size=64)

# Run through each pixel individually and turn it on.
#for x in range(8):
#	for y in range(8):
#		# Clear the display buffer.
#		display.clear()
#		# Set pixel at position i, j to on.  To turn off a pixel set
#		# the last parameter to 0.
#		display.set_pixel(x, y, 1)
#		# Write the display buffer to the hardware.  This must be called to
#		# update the actual display LEDs.
#		display.write_display()
#		# Delay for half a second.
#		time.sleep(0.1)


# for _ in range(500):
#   pts = np.random.randint(2, size=64)
#   display.clear()
#   for i, v in enumerate(pts):
#     display.set_pixel(i//8, i%8, v)
#   display.write_display()
#   time.sleep(0.25)

# Draw some shapes using the Python Imaging Library.

# Clear the display buffer.
# display.clear()
#time.sleep(0.25)

# First create an 8x8 1 bit color image.
#image = Image.new('1', (8, 8))

# Then create a draw instance.
#draw = ImageDraw.Draw(image)

# Draw a rectangle with colored outline
#draw.rectangle((0,0,7,7), outline=255, fill=0)

# Draw an X with two lines.
#draw.line((1,1,6,6), fill=255)
#draw.line((1,6,6,1), fill=255)

# Draw the image on the display buffer.
#display.set_image(image)

# Draw the buffer to the display hardware.
# display.write_display()

# See the SSD1306 library for more examples of using the Python Imaging Library
# such as drawing text: https://github.com/adafruit/Adafruit_Python_SSD1306
