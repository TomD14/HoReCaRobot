# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

import re

from tof_i2c import TOF10120
tof=TOF10120()

import network
from machine import Pin
from neopixel import NeoPixel
import time
import math

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

class LightControls:

    def __init__(self): # dit is de constructor, wordt uitgevoerd tijdens object creatie
            self.size = 30
            self.p = Pin(15)
            self.pn = NeoPixel(self.p,30,bpp=4)

    def Left(self):
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if 5 > i:
                self.pn[p] = (255,0,0,0)
                print(p)
            else:
                self.pn[p] = (0,32,0,0)
                print('Green')
            i = i+1
                
        self.pn.write()
            
    def Front(self):
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if i > 5 and i < 11:
                self.pn[p] = (255,0,0,0)
                print('rood')
                print(p)
            else:
                self.pn[p] = (0,32,0,0)
                print('green')
                print(i)
                    
            i = i+1
        self.pn.write()
        
    def Right(self):
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if i > 11 and i < 17:
                self.pn[p] = (255,0,0,0)
                print('rood')
                print(p)
            else:
                self.pn[p] = (0,32,0,0)
                print('green')
                print(i)
                    
            i = i+1
        self.pn.write()
            
            
    def Closing(self, side, distance, ledWidth):
        i = side - ledWidth
        y = 1 + ledWidth*2
        x = math.floor(2000 / y)
        greenRange = 0
        redRange = 0 - math.ceil(y/2)
        green = math.ceil(y/2)
        red = green*2
        Semitop = x*(y - 1)
        
        while y >= 0:
            cap = x*y
            if cap != 0:
                print('y value = ' + str(y))
                print('x*y value = ' + str(x*y))
                if distance <= 2000 and distance > Semitop and green >= 1:
                    offLeds = i
                    while offLeds <= side + ledWidth:
                        if offLeds == side:
                            self.pn[offLeds] = (0,60,0,0)
                        else:
                            self.pn[offLeds] = (0,0,0,0)
                        offLeds = offLeds + 1
                elif distance <= x*y and distance > x*(y-1) and green >= 1:
                    leds = i + green - 1
                    offLeds = i
                    while offLeds <= side + ledWidth:
                        if offLeds == leds and leds <= side + greenRange:
                            print('GROENE ledjes = ' + str(leds))
                            print('TOP limiet = ' + str(side + greenRange))
                            self.pn[offLeds] = (0,60,0,0)
                            leds = leds + 1
                        else:
                            self.pn[offLeds] = (0,0,0,0)
                        offLeds = offLeds + 1
                            
                elif distance <= x*y and distance > x*(y-1) and green <= 0:
                    leds = i + red - 1
                    offLeds = i
                    while offLeds <= side + ledWidth:
                        if offLeds == leds and leds <= side + redRange:
                            print('ROODe ledjes = ' + str(leds))
                            self.pn[leds] = (60,0,0,0)
                            leds = leds + 1
                        else:
                            self.pn[offLeds] = (0,60,0,0)
                        offLeds = offLeds + 1

            elif distance <= 100:
                leds = i
                print('bodem waarde')
                while leds <= side + ledWidth:
                    self.pn[leds] = (60,0,0,0)
                    leds = leds + 1
            green = green - 1
            red = red - 1
            y = y - 1
            greenRange = greenRange + 1
            redRange = redRange + 1
            
        self.pn.write()
                

                    
            
    def Back(self):
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if i > 17 and i < 23:
                self.pn[p] = (255,0,0,0)
                print('rood')
                print(p)
            else:
                self.pn[p] = (0,32,0,0)
                print('green')
                print(i)
                    
            i = i+1
        self.pn.write()
            
    def off(self):
        for p in range(self.pn.n):
            # print(p)
            self.pn[p] = (0,0,0,0)
        self.pn.write()

    def web_page(self):
      html = """
        <html>
        <head>
        <title>ESP Web Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
          h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
          .button{display: inline-block; background-color: #e7bd3b; border: none; 
          border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
          .button2{background-color: #4286f4;}
          .button3{background-color: #10E109;}
        </style>
        </head>
        <body> <h1>ESP Web Server</h1> 
          <p><a href="/?NeoFront"><button class="button">Front</button></a></p>
          <p><a href="/?NeoLeft"><button class="button">Left</button></a>
          <a href="/?NeoRight"><button class="button">Right</button></a></p>
          <p><a href="/?NeoBack"><button class="button">Back</button></a></p>
          <form action="/get">
            afstand tot sensor: <input type="number" name="input1">
            <input type="submit" value="Submit">
          </form>
          <form action="/get">
            led breedte: <input type="number" name="input2">
            <input type="submit" value="Submit">
          </form>
          <p><a href="/?NeoDistanceToggleON"><button class="button button3">TOF example 10 sec/button></a></p>
          <p><a href="/?NeoOff"><button class="button button2">OFF</button></a></p>
        </body>
        </html>
        """
      return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

LC = LightControls()

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % str(request))
    Left = request.find('/?NeoLeft')
    Off = request.find('/?NeoOff')
    Front = request.find('/?NeoFront')
    Right = request.find('/?NeoRight')
    Back = request.find('/?NeoBack')
    toggleon = request.find('/?NeoDistanceToggleON')
    ManualInput1 = request.find('/get?input1=')
    ManualInput2 = request.find('/get?input2=')
    
    ToggleBool = 1
    extrabool = 0

    if toggleon == 6:
        ToggleBool = 0
        print('TOF On')
        counter = 0
        
    if Left == 6:
        LC.Left()
        print('Left')
    if Off == 6:
        LC.off()
        print('off')
    if Front == 6:
        LC.Front()
        print('Front')
    if Right == 6:
        LC.Right()
        print('Right')
    if Back == 6:
        LC.Back()
        print('Back')
    if ManualInput1 == 6:
        num = request.find('HTTP')
        input1 = int(request[18:num])
        LC.Closing(0, input1, maxLeds)
        print('Closing ' + str(input1) + ' distance')
    if ManualInput2 == 6:
        maxLeds = int(request[18:19])
        print('new maxLeds = ' + str(maxLeds))
        
    while ToggleBool == 0:
        time.sleep_ms(100)
        distance = tof.get_distance_filtered()
        print(distance)
        LC.Closing(10, distance, maxLeds)
        counter = counter + 1
        print('distance ' + str(distance))
        print('tijd ' + str(counter))
        if counter >= 100:
            ToggleBool = 1
            LC.off()
    
        
        
    response = LC.web_page()
    conn.send(response)
    conn.close()
    

    
