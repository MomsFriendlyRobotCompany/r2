# import time

#from PIL import Image
#from PIL import ImageDraw
import numpy as np

try:
    from Adafruit_LED_Backpack.Matrix8x8 import Matrix8x8
except ImportError:
    from .fake import Matrix8x8


class Randomizer(object):
    def __init__(self, size=10):
        self.pts = np.random.randint(2, size=64*size)
        self.size = size
        self.cnt = 0

    def get(self):
        ret = self.pts[self.cnt:self.cnt + 64]
        # self.cnt += 1
        self.cnt = (self.cnt + 1) % self.size
        return ret


class MatrixArray(object):
    def __init__(self, ids, brightness=14):
        self.lcds = []
        self.rand = Randomizer(20)
        for id in ids:
            self.lcds.append(Matrix8x8(address=id))

        if 15 < brightness < 0:
            raise Exception("MatrixArray::brightness must be 0-15:", brightness)

        for lcd in self.lcds:
            lcd.begin()
            lcd.set_brightness(brightness)
            lcd.clear()
            lcd.write_display()

    def __del__(self):
        for lcd in self.lcds:
            lcd.clear()
            lcd.write_display()

    def random(self, lcds=None):
        for lcd in self.lcds:
            # pts = np.random.randint(2, size=64)
            pts = self.rand.get()
            lcd.clear()
            for i, v in enumerate(pts):
                lcd.set_pixel(i//8, i % 8, v)
            lcd.write_display()
