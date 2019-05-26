from time import sleep
from Sounds import Sounds
import time
import random
from Hardware import Actuators, Sensors, Displays
from pygecko import FileStorage
# from multiprocessing import Process
import string


def idle(ns, run):
    while run.is_set():
        sleep(1)


def chaos(ns, run):
    """
    This does NOTHING USEFUL!!!!!!!
    It just exercises the codebase
    """
    sensors = Sensors()
    servos = Actuators()
    snd = Sounds()

    fs = FileStorage()
    fs.readJson("clips.json")
    clips = fs.db

    while run.is_set():
        # update display
        # logic_displays.update()

        # read inputs
        # ps4 = js.get()
        # print(ps4)

        # play random clip
        clip = random.choice(clips.keys())
        print('playing:', clip)
        snd.sound(clip)
        time.sleep(5)

        # speak random word
        char_set = string.ascii_lowercase
        word = ''.join(random.sample(char_set, 6))
        snd.speak(word)
        time.sleep(3)

        # move random servo
        num = random.choice(range(3))
        name = 'door{}'.format(num)
        angle = random.choice(range(30, 150, 10))
        print('Moving servro:', name, angle)
        servos.set(name, angle)
        time.sleep(1)
