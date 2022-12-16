from machine import Pin
from neopixel import NeoPixel
import time
import math

class DistanceMethods:
    
    def __init__(self):
        self.size = 60 
        self.p1 = Pin(15)
        self.p2 = Pin(16)
        self.p3 = Pin(17)
        self.pn1 = NeoPixel(self.p1,self.size,bpp=4)
        self.pn2 = NeoPixel(self.p2,self.size,bpp=4)
        self.pn3 = NeoPixel(self.p3,self.size,bpp=4)
        
    
    def off(self):
        
        for p in range(self.pn2.n):
            self.pn2[p] = (0,0,0,0)
        self.pn2.write()
    
    
    def ClosingPulse(self, side, distance, ledWidth):
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
                            self.pn2[offLeds] = (0,60,0,0)
                        else:
                            self.pn2[offLeds] = (0,0,0,0)
                        offLeds = offLeds + 1
                elif distance <= x*y and distance > x*(y-1) and green >= 1:
                    leds = i + green - 1
                    offLeds = i
                    while offLeds <= side + ledWidth:
                        if offLeds == leds and leds <= side + greenRange:
                            print('GROENE ledjes = ' + str(leds))
                            print('TOP limiet = ' + str(side + greenRange))
                            self.pn2[offLeds] = (0,60,0,0)
                            leds = leds + 1
                        else:
                            self.pn2[offLeds] = (0,0,0,0)
                        offLeds = offLeds + 1
                                
                elif distance <= x*y and distance > x*(y-1) and green <= 0:
                    leds = i + red - 1
                    offLeds = i
                    while offLeds <= side + ledWidth:
                        if offLeds == leds and leds <= side + redRange:
                            print('ROODe ledjes = ' + str(leds))
                            self.pn2[leds] = (60,0,0,0)
                            leds = leds + 1
                        else:
                            self.pn2[offLeds] = (0,60,0,0)
                        offLeds = offLeds + 1

            elif distance <= 100:
                leds = i
                print('bodem waarde')
                while leds <= side + ledWidth:
                    self.pn2[leds] = (60,0,0,0)
                    leds = leds + 1
            green = green - 1
            red = red - 1
            y = y - 1
            greenRange = greenRange + 1
            redRange = redRange + 1
                
        self.pn2.write()
            
            
    def ClosingRed(self):
        x = 20
        i = 10
        y = 200
        while x <= 250:
            z = 0 - math.floor(x / 50)
            print(z)
            while z <= 2:
                for p in range(self.pn2.n):
                    self.pn2[p] = (x, 0, 0, 0)
                self.pn2.write()
                time.sleep_ms(y)
                if x >= 50:
                    for p in range(self.pn2.n):
                        self.pn2[p] = (x - i, 0, 0, 0)
                else:
                    for p in range(self.pn2.n):
                        self.pn2[p] = (10, 0, 0, 0)
                self.pn2.write()
                time.sleep_ms(y)
                z = z + 1
            y = y - 15
            i = i + 15
            x = x + 50
    
    
    def ClosingStoplichtBlink(self):
        x = 0
        while x <= 2:
            z = 0
            for p in range(self.pn2.n):
                if z > 12 and z < 18:
                    self.pn2[p] = (0,255,0,0)
                        
                z = z+1
            self.pn2.write()
            time.sleep_ms(500)
            y = 0
            for p in range(self.pn2.n):
                if y > 12 and y < 18:
                    self.pn2[p] = (0,200,0,0)
                        
                y = y+1
            self.pn2.write()
            time.sleep_ms(500)
            x = x+1
        time.sleep_ms(500)
        
        x = 0
        while x <= 4:
            z = 0
            for p in range(self.pn2.n):
                if z > 12 and z < 18:
                    self.pn2[p] = (255,150,0,0)
                        
                z = z+1
            self.pn2.write()
            time.sleep_ms(300)
            y = 0
            for p in range(self.pn2.n):
                if y > 12 and y < 18:
                    self.pn2[p] = (150,80,0,0)
                        
                y = y+1
            self.pn2.write()
            time.sleep_ms(300)
            x = x+1
        time.sleep_ms(100)
        
        x = 0
        while x <= 12:
            z = 0
            for p in range(self.pn2.n):
                if z > 12 and z < 18:
                    self.pn2[p] = (255,0,0,0)
                        
                z = z+1
            self.pn2.write()
            time.sleep_ms(100)
            y = 0
            for p in range(self.pn2.n):
                if y > 12 and y < 18:
                    self.pn2[p] = (200,0,0,0)
                        
                y = y+1
            self.pn2.write()
            time.sleep_ms(100)
            x = x+1
            
            
    def ClosingSwipe(self):
        p = 0
        y = 10
        z = 16
        t = 150
        while p <= 6:
            u = 16
            l = 17
            m = 10
            self.pn2[15] = (0, 0, 0, 0)
            while u >= y:
                self.pn2[u] = (255, 0, 0, 0)
                self.pn2[l] = (0, 0, 0, 0)
                u = u - 1
                l = l - 1
                self.pn2.write()
                time.sleep_ms(t)
            t = t - 10
            u = 11
            
            while u <= 15:
                if u <= z:
                    self.pn2[u] = (255, 0, 0, 0)
                self.pn2[m] = (0, 0, 0, 0)
                u = u + 1
                m = m + 1
                self.pn2.write()
                time.sleep_ms(t)
            t = t - 10
            p = p + 1
  
        x = 16
        z = 10
        while x >= z:
            self.pn2[x] = (255, 0, 0, 0)
            x = x - 1
        self.pn2.write()