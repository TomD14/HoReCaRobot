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

DS = DistanceMethods()
LC = LightControls()
SM = SidesMethods()


while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % str(request))
    
    LeftScenario1 = request.find('/?LeftScenario1')
    LeftScenario2 = request.find('/?LeftScenario2')
    LeftScenario3 = request.find('/?LeftScenario3')
    LeftScenario4 = request.find('/?LeftScenario4')
    LeftScenario5 = request.find('/?LeftScenario5')
    
    RightScenario1 = request.find('/?RightScenario1')
    RightScenario2 = request.find('/?RightScenario2')
    RightScenario3 = request.find('/?RightScenario3')
    RightScenario4 = request.find('/?RightScenario4')
    RightScenario5 = request.find('/?RightScenario5')
    
    ClosingScenario1 = request.find('/?ClosingScenario1')
    ClosingScenario2 = request.find('/?ClosingScenario2')
    ClosingScenario3 = request.find('/?ClosingScenario3')
    ClosingScenario4 = request.find('/?ClosingScenario4')
    
    BrakeScenario1 = request.find('/?BrakeScenario1')
    BrakeScenario2 = request.find('/?BrakeScenario2')
    BrakeScenario3 = request.find('/?BrakeScenario3')
    
    DriveScenario1 = request.find('/?DriveScenario1')
    DriveScenario2 = request.find('/?DriveScenario2')
    DriveScenario3 = request.find('/?DriveScenario3')
    
    Off = request.find('/?NeoOff')
    ManualInput1 = request.find('/get?input1=')
    
    ToggleBool = 1
    toggleon = 0
    
    if LeftScenario1 == 6:
        SM.SideAnimationFullLEFT()
    
    if LeftScenario2 == 6:
        SM.SideAnimationPartLEFT()
    
    if LeftScenario3 == 6:
        SM.SideFullRotationLEFT()
    
    if LeftScenario4 == 6:
        SM.SideFadeLEFT()
    
    if LeftScenario5 == 6:
        SM.SideBlinkerLEFT()
        
    
    if RightScenario1 == 6:
        SM.SideAnimationFullRIGHT()
    
    if RightScenario2 == 6:
        SM.SideAnimationPartRIGHT()
    
    if RightScenario3 == 6:
        SM.SideFullRotationRIGHT()
    
    if RightScenario4 == 6:
        SM.SideFadeRIGHT()
    
    if RightScenario5 == 6:
        SM.SideBlinkerRIGHT()
        
        
    if BrakeScenario1 == 6:
        SM.BrakePulse()
    
    if BrakeScenario2 == 6:
        SM.BrakeBlink()
    
    if BrakeScenario3 == 6:
        SM.BrakeFade()
        
        
    if DriveScenario1 == 6:
        SM.DrivePulse()
    
    if DriveScenario2 == 6:
        SM.DriveBlink()
    
    if DriveScenario3 == 6:
        SM.DriveFade()
    
    
    if ClosingScenario1 == 6:
        x = 2000
        while x >= 0:
            DS.ClosingPulse(8, x, 1)
            time.sleep_ms(100)
            x = x - 100
    
    if ClosingScenario2 == 6:
        DS.ClosingStoplichtBlink()
    
    if ClosingScenario3 == 6:
        DS.ClosingRed()
        
    if ClosingScenario4 == 6:
        DS.ClosingSwipe()
        
        
    if Off == 6:
        DS.off()
        SM.off()
        print('off')
        
        
    if ManualInput1 == 6:
        num = request.find('HTTP')
        input1 = int(request[18:num])
        DS.Closing(compasSide, input1, maxLeds)
        print('Closing ' + str(input1) + ' distance')
    
        
    if toggleon == 6:
        ToggleBool = 0
        print('TOF On')
        counter = 0
    
    while ToggleBool == 0:
        time.sleep_ms(100)
        distance = tof.get_distance_filtered()
        print(distance)
        DS.Closing(10, distance, maxLeds)
        counter = counter + 1
        print('distance ' + str(distance))
        print('tijd ' + str(counter))
        if counter >= 100:
            ToggleBool = 1
            LC.off()
     
        
    response = WebPage()
    conn.send(response)
    conn.close()