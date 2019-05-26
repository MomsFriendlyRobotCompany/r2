#!/usr/bin/env python

from pygecko.multiprocessing import geckopy
from pygecko.multiprocessing import GeckoSimpleProcess
import time

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

    start = time.time()
    cnt = 0
    while not geckopy.is_shutdown():
        msg = {'time': time.time() - start}
        p.publish(msg)  # topic msg

        geckopy.logdebug('[{}] published msg'.format(cnt))
        cnt += 1
        rate.sleep()
    print('pub bye ...')


def camera_pub():
    geckopy.init_node()
    rate = geckopy.Rate(2)

    p = geckopy.pubBinderTCP(
        KEY,
        "camera"
    )

    if p is None:
        raise Exception("publisher is None")

    start = time.time()
    cnt = 0
    while not geckopy.is_shutdown():
        msg = {'time': time.time() - start}
        p.publish(msg)  # topic msg

        geckopy.logdebug('[{}] published msg'.format(cnt))
        cnt += 1
        rate.sleep()
    print('pub bye ...')


def subscriber():
    geckopy.init_node()
    rate = geckopy.Rate(2)

    s = geckopy.subConnectTCP(
        KEY,
        "test"
    )

    if s is None:
        raise Exception("subscriber is None")

    while not geckopy.is_shutdown():
        msg = s.recv_nb()
        if msg:
            geckopy.loginfo("{}: {}".format(msg))
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

    p = GeckoSimpleProcess()
    p.start(func=imu_pub, name='imu_pub')
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
