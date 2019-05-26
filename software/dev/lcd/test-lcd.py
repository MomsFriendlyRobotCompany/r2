#!/usr/bin/env python
import netifaces as nf
import psutil as ps
import socket
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class OLED(object):
    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        self.font = font = ImageFont.load_default()
        self.image = image = Image.new('1', (self.disp.width, self.disp.height))
        self.draw = ImageDraw.Draw(self.image)

    def __del__(self):
        self.disp.clear()
        self.disp.display()

    def run(self):
        # https://github.com/sindresorhus/cli-spinners/blob/HEAD/spinners.json
        # spin = ['|','/','-','\\','+']
        spin = ['|','/','--','\\']
        # spin = ["◴","◷","◶","◵"]
        # spin = ["◐","◓","◑","◒"]
        # spin = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
        wrap = len(spin)
        i = 0
        try:
            while True:
                # self.disp.clear()
                self.draw.rectangle((0,0,self.disp.width,self.disp.height), outline=0, fill=0)

                # get interfaces
                ifs = nf.interfaces()
                ap = False
                if 'wlan1' in ifs:
                    addr = nf.ifaddresses('wlan0')[nf.AF_INET][0]['addr']
                    if addr == '10.10.10.1':
                        ap = True
                addrs = []
                for ip in ['en0', 'eth0', 'wlan0']:
                    if ip in ifs:
                        addr = nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
                        addrs.append((ip, addr,))

                line1 = "{} AP[{}] {}".format(
                    socket.gethostname().split('.')[0],
                    'UP' if ap else 'DOWN',
                    spin[i%wrap]
                )
                i += 1

                ystart = -2
                fillval = 255

                self.draw.text((0, ystart), line1,  font=self.font, fill=fillval)

                cpu = ps.cpu_percent()
                mem = ps.virtual_memory().percent
                line2 = "CPU: {:3.0f}% Mem: {:3.0f}%".format(cpu,mem)

                self.draw.text((0, ystart+8), line2,  font=self.font, fill=fillval)

                offset = 16
                for ip, addr in addrs:
                    s = "{}: {}".format(ip, addr)
                    self.draw.text((0,ystart+offset), s,  font=self.font, fill=fillval)
                    offset += 8

                # self.draw.text((0,0), "hi",  font=self.font, fill=127)
                self.disp.image(self.image)
                self.disp.display()
                time.sleep(1)
        except KeyboardInterrupt:
            print('bye ...')
        except Exception as e:
            print("ERROR:", e)
            exit(1)


lcd = OLED()
lcd.run()
