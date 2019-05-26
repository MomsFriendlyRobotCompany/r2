import numpy as np


class IMU(object):
    def __init__(self, gs=2, dps=250, verbose=False):
        print("FAKE nxp_imu")

    def __del__(self):
        pass

    def get(self):
        return tuple([0]*9)


class PCA9685(object):
    def __init__(self):
        print("FAKE PCA9685")

    def set_pwm_freq(self, pwm):
        pass

    def set_all_pwm(self, a, b):
        pass

    def set_pwm(self, a, b, c):
        pass


class BGR(object):
    """Fake class"""

    def __init__(self, sz):
        # constructor
        self.array = np.random.rand(*sz)

    def truncate(self, num):
        # refreshes the fake image
        self.array = np.random.rand(*self.array.shape)


# class picamera(object):
#     """Fake class"""
class PiCamera(object):
    """Fake class"""
    resolution = (0, 0)

    def __init__(self):
        pass

    def close(self):
        # this does nothing
        pass

    def capture(self, image, format, use_video_port):
        # this does nothing
        pass


class array(object):
    """Fake class"""

    @staticmethod
    def PiRGBArray(cam, size):
        return BGR(size)
