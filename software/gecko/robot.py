#!/usr/bin/env python

from pygecko.multiprocessing import geckopy
from pygecko.multiprocessing import GeckoSimpleProcess
import time

from lib.led_matrix import MatrixArray
from lib.servo import Servo

try:
    from nxp_imu import IMU as NXP_IMU
except ImportError:
    from lib.fake import NXP_IMU

try:
    from picamera import PiCamera
except ImportError:
    from lib.fake import PiCamera

# from imutils.video import VideoStream
# vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
# frame = vs.read()

KEY = "logan"


def imu_pub():
    geckopy.init_node()
    rate = geckopy.Rate(2)

    p = geckopy.pubBinderTCP(
        KEY,
        "imu"
    )

    if p is None:
        raise Exception("publisher is None")

    imu = NXP_IMU()

    while not geckopy.is_shutdown():
        msg = imu.get()
        p.publish(msg)  # topic msg
        rate.sleep()
    print('imu pub bye ...')


def camera_pub():
    geckopy.init_node()
    rate = geckopy.Rate(2)

    p = geckopy.pubBinderTCP(
        KEY,
        "camera"
    )

    if p is None:
        raise Exception("publisher is None")

    cam = PiCamera()
    while not geckopy.is_shutdown():
        # img = cam.read()
        img = True
        if img:
            msg = "hi"
            p.publish(msg)
        rate.sleep()
    print('camera pub bye ...')


def matrix_sub():
    geckopy.init_node()
    rate = geckopy.Rate(10)

    # s = geckopy.subConnectTCP(
    #     KEY,
    #     "test"
    # )
    #
    # if s is None:
    #     raise Exception("subscriber is None")

    m = MatrixArray([0x70, 0x71, 0x72, 0x73], brightness=0)

    while not geckopy.is_shutdown():
        # msg = s.recv_nb()
        # if msg:
        #     geckopy.loginfo("{}: {}".format(msg))
        m.random()
        rate.sleep()

    print('sub bye ...')


if __name__ == '__main__':
    # normally you wouldn't run this here, but is running else where
    # this is just for testing
    # from pygecko.transport import GeckoCore
    # core = GeckoCore()
    # core.start()

    # although I don't do anything with procs, because I reuse the variables
    # p and s below, they will kill the processes when new process are created
    # using those names. Appending them to procs allows me to keep them alive
    # until the program ends
    procs = []

    run = [
        imu_pub,
        camera_pub,
        matrix_sub
    ]

    for func in run:
        p = GeckoSimpleProcess()
        p.start(func=func)
        procs.append(p)

    # s = GeckoSimpleProcess()
    # s.start(func=subscriber, name='sub_{}'.format(topic), kwargs=args)
    # procs.append(s)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('main process got ctrl-c')
            break
