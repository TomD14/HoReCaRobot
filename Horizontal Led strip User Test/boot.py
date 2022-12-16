try:
  import usocket as socket
except:
  import socket

import re

from tof_i2c import TOF10120
tof=TOF10120()

import Site
import network
from machine import Pin
from neopixel import NeoPixel
import time
import math
from Site import WebPage
from Distance import DistanceMethods
from Sides import SidesMethods
from BrakeDrive import BrakeDriveMethods

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'MicroPython-AP'
password = 'ESPHoeWerktDit'


ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
ap.config(authmode=3)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

led = Pin(22, Pin.OUT)
counter = 0
maxLeds = 1
compasSide = 3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
