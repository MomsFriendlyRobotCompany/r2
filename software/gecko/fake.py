import numpy as np


class NXP_IMU(object):
    def __init__(self, gs=2, dps=250, verbose=False):
        print("FAKE nxp_imu")
        self.an = np.random.normal(0, 0.001, 3*1000)
        self.gn = np.random.normal(0, 0.2, 3*1000)
        self.mn = np.random.normal(0, 0.5, 3*1000)
        self.cnt = 0

    def __del__(self):
        pass

    def get(self):
        """
        This is based of some static reading I took.
        returns (accel, mag, gyro)
        """
        ret = self.an[self.cnt:self.cnt+3] + self.gn[self.cnt:self.cnt+3] + self.mn[self.cnt:self.cnt+3]
        ret[2] += 1.0

        # magnetometer
        ret[3] += -22
        ret[4] += -5
        ret[5] += 9

        self.cnt += 3
        self.cnt %= 3*1000
        return tuple(ret)


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
