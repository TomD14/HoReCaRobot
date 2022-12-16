from machine import Pin
from neopixel import NeoPixel
import time
import math

Range = 2

class SidesMethods:

    def __init__(self):
            self.size = 60 
            self.p1 = Pin(15)
            self.p2 = Pin(16)
            self.p3 = Pin(17)
            self.pn1 = NeoPixel(self.p1,self.size,bpp=4)
            self.pn2 = NeoPixel(self.p2,self.size,bpp=4)
            self.pn3 = NeoPixel(self.p3,self.size,bpp=4)
            
            
    def off(self):
        for p in range(self.pn1.n):
            self.pn1[p] = (0,0,0,0)
        self.pn1.write()
        
        for p in range(self.pn2.n):
            self.pn2[p] = (0,0,0,0)
        self.pn2.write()
        
        for p in range(self.pn3.n):
            self.pn3[p] = (0,0,0,0)
        self.pn3.write()
    

    

    def SideAnimationPartLEFT(self):
        v = 0
        while v <= 2:
            i = 48
            j = 43
            while i <= 59:
                self.pn1[i] = (255, 0, 0, 0)
                
                if j >= 48:
                    self.pn1[j] = (0, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
            i = 0
            g = -5
            while i <= 10:
                if i <= 10:
                    self.pn1[i] = (255, 0, 0, 0)
                
                if j <= 59:
                    self.pn1[j] = (0, 0, 0, 0)
                elif g >=0:
                    self.pn1[g] = (0, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
                g = g + 1
            
            i = 48
            j = 43
            while i <= 59:
                self.pn1[i] = (255, 0, 0, 0)
                
                if g <= 10:
                    self.pn1[g] = (0, 0, 0, 0)
                
                if j >= 48:
                    self.pn1[j] = (0, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
                g = g + 1
            i = 0
            g = -5
            while g <= 10:
                if i <= 10:
                    self.pn1[i] = (255, 0, 0, 0)
                
                if j <= 59:
                    self.pn1[j] = (0, 0, 0, 0)
                elif g >=0:
                    self.pn1[g] = (0, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
                g = g + 1
            v = v + 1
            
    
    def SideAnimationPartRIGHT(self):
        v = 0
        while v <= 2:
            i = 40
            j = 45
            while i >= 18:
                self.pn1[i] = (255, 0, 0, 0)
                
                if j <= 40:
                    self.pn1[j] = (0, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i - 1
                j = j - 1
                
            k = 40
            l = 45
            while l >= 18:
                if k >= 18:
                    self.pn1[k] = (255, 0, 0, 0)
                    
                if j >= 18:
                    self.pn1[j] = (0, 0, 0, 0)

                if l >= 18 and l <= 40:
                    self.pn1[l] = (0, 0, 0, 0)

                self.pn1.write()    
                time.sleep_ms(50)
                k = k - 1
                l = l - 1
                j = j - 1
            v = v+1
        
        
    def SideAnimationFullLEFT(self):
        z = 0
        while z <= 1:
            i = 48
            while i <= 59:
                self.pn1[i] = (255, 0, 0, 0)
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
            
            i = 0
            while i <= 10:
                self.pn1[i] = (255, 0, 0, 0)
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                
            j = 48
            while j <= 59:
                self.pn1[j] = (0, 0, 0, 0)
                self.pn1.write()
                time.sleep_ms(50)
                j = j + 1
            
            j = 0
            while j <= 10:
                self.pn1[j] = (0, 0, 0, 0)
                self.pn1.write()
                time.sleep_ms(50)
                j = j + 1
            z = z + 1
            
    def SideAnimationFullRIGHT(self):
        z = 0
        while z <= 1:
            i = 40
            while i >= 18:
                self.pn1[i] = (255, 0, 0, 0)
                self.pn1.write()
                time.sleep_ms(50)
                i = i - 1
            j = 40
            while j >= 18:
                self.pn1[j] = (0, 0, 0, 0)
                self.pn1.write()
                time.sleep_ms(50)
                j = j - 1
            z = z + 1
            
    
    def SideFullRotationLEFT(self):
        x = 18
        y = 48
        
        rotations = 0
        t = 13
        r = 43
        while rotations <= 3:
            while y <= 59:
                self.pn1[x] = (255, 0, 0, 0)
                self.pn1[y] = (255, 0, 0, 0)
                if t >= 18:
                    self.pn1[t] = (0, 0, 0, 0)
                    self.pn1[r] = (0, 0, 0, 0)
                time.sleep_ms(100)
                self.pn1.write()
                x = x + 1
                y = y + 1
                t = t + 1
                r = r + 1
            
            z = 0
            p = -5
            while p <= 10:
                if x <= 40:
                    self.pn1[x] = (255, 0, 0, 0)
                    self.pn1[z] = (255, 0, 0, 0)
                if t <= 40:
                    self.pn1[t] = (0,0,0,0)
                if p >= 0:
                    self.pn1[p] = (0,0,0,0)
                if r <= 59:
                    self.pn1[r] = (0,0,0,0)
                time.sleep_ms(100)
                self.pn1.write()
                x = x + 1
                z = z + 1
                p = p + 1
                t = t + 1
                r = r + 1
            rotations = rotations + 1
            
            
    def SideFullRotationRIGHT(self):
        x = 40
        y = 10
        rotations = 0
        t = 45
        r = 15
        
        while rotations <= 3:
            while y >= 0:
                self.pn1[x] = (255, 0, 0, 0)
                self.pn1[y] = (255, 0, 0, 0)
                if t <= 40:
                    self.pn1[t] = (0, 0, 0, 0)
                    self.pn1[r] = (0, 0, 0, 0)
                time.sleep_ms(100)
                self.pn1.write()
                x = x - 1
                y = y - 1
                t = t - 1
                r = r - 1
            
            z = 59
            p = 64
            while p >= 48:
                if x >= 18:
                    self.pn1[x] = (255, 0, 0, 0)
                    self.pn1[z] = (255, 0, 0, 0)
                if t >= 18:
                    self.pn1[t] = (0,0,0,0)
                if p <= 59:
                    self.pn1[p] = (0,0,0,0)
                if r >= 0:
                    self.pn1[r] = (0,0,0,0)
                time.sleep_ms(100)
                self.pn1.write()
                x = x - 1
                z = z - 1
                p = p - 1
                t = t - 1
                r = r - 1
            rotations = rotations + 1
     
     
    def SideBlinkerLEFT(self):
        l = 0
        z = 0
        
        while z <= 4:
            q = 48
            w = 0
            if l == 0:
                l = 1
            else:
                l = 0
                
            while q <= 59:
                print(l)
                if l == 0:
                    self.pn1[q] = (255, 0, 0, 0)
                    if w <= 10:
                        self.pn1[w] = (255, 0, 0, 0)
                    l = 1
                else:
                    self.pn1[q] = (50, 0, 0, 0)
                    if w <= 10:
                        self.pn1[w] = (50, 0, 0, 0)
                    l = 0
                q = q + 1
                w = w + 1
            self.pn1.write()
            time.sleep_ms(1000)
            z = z + 1
        
        q = 48
        w = 0
        while q <= 59:
            self.pn1[q] = (0, 0, 0, 0)
            self.pn1[w] = (0, 0, 0, 0)
            q = q + 1
            w = w + 1
        self.pn1.write()
    
    
    def SideBlinkerRIGHT(self):
        l = 0
        z = 0
        
        while z <= 4:
            q = 18
                
            while q <= 40:
                print(z)
                if l == 0:
                    self.pn1[q] = (255, 0, 0, 0)
                    print('hIGH')
                    l = 1
                else:
                    self.pn1[q] = (50, 0, 0, 0)
                    print('Low')
                    l = 0
                q = q + 1
            self.pn1.write()
            time.sleep_ms(1000)
            z = z + 1
        
        q = 18
        while q <= 40:
            self.pn1[q] = (0, 0, 0, 0)
            q = q + 1
        self.pn1.write()
     
           
    def SideFadeLEFT(self):
        q = 48
        w = 0
        while w <= 10:
            if q <= 59:
                self.pn1[q] = (50, 0, 0, 0)
                q = q + 1
            else:
                self.pn1[w] = (50, 0, 0, 0)
                w = w + 1
            time.sleep_ms(40)
            self.pn1.write()
        
        v = 0
        while v <= 1:
            i = 48
            j = 43
            while i <= 59:
                self.pn1[i] = (255, 0, 0, 0)
                
                if j >= 48:
                    self.pn1[j] = (50, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
            i = 0
            g = -5
            while i <= 10:
                if i <= 10:
                    self.pn1[i] = (255, 0, 0, 0)
                
                if j <= 59:
                    self.pn1[j] = (50, 0, 0, 0)
                elif g >=0:
                    self.pn1[g] = (50, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
                g = g + 1
            
            i = 48
            j = 43
            while i <= 59:
                self.pn1[i] = (255, 0, 0, 0)
                
                if g <= 10:
                    self.pn1[g] = (50, 0, 0, 0)
                
                if j >= 48:
                    self.pn1[j] = (50, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
                g = g + 1
            i = 0
            g = -5
            while g <= 10:
                if i <= 10:
                    self.pn1[i] = (255, 0, 0, 0)
                
                if j <= 59:
                    self.pn1[j] = (50, 0, 0, 0)
                elif g >=0:
                    self.pn1[g] = (50, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i + 1
                j = j + 1
                g = g + 1
            v = v + 1
        
        q = 48
        w = 0
        while w <= 10:
            if q <= 59:
                self.pn1[q] = (0, 0, 0, 0)
                q = q + 1
            else:
                self.pn1[w] = (0, 0, 0, 0)
                w = w + 1
            time.sleep_ms(40)
            self.pn1.write()
           
           
    def SideFadeRIGHT(self):
        q = 40
        while q >= 18:
            self.pn1[q] = (50, 0, 0, 0)
            q = q - 1
            self.pn1.write()
            time.sleep_ms(40)
        
        v = 0
        while v <= 1:
            i = 40
            j = 45
            while i >= 18:
                self.pn1[i] = (255, 0, 0, 0)
                
                if j >= 18 and j <= 40:
                    self.pn1[j] = (50, 0, 0, 0)
                    
                self.pn1.write()
                time.sleep_ms(50)
                i = i - 1
                j = j - 1
                
            k = 40
            l = 45
            while l >= 18:
                if k >= 18:
                    self.pn1[k] = (255, 0, 0, 0)
                    
                if j >= 18:
                    self.pn1[j] = (50, 0, 0, 0)

                if l >= 18 and l <= 40:
                    self.pn1[l] = (50, 0, 0, 0)

                self.pn1.write()    
                time.sleep_ms(50)
                k = k - 1
                l = l - 1
                j = j - 1
            v = v+1
            
        q = 40
        while q >= 18:
            self.pn1[q] = (0, 0, 0, 0)
            q = q - 1
            self.pn1.write()
            time.sleep_ms(40)
           
           
           
    
    def BrakePulse(self):

        self.pn1[14] = (255, 0, 0, 0)
        self.pn1[44] = (255, 0, 0, 0) 
        self.pn1.write()
        time.sleep_ms(500)
        
        i = math.floor(Range/2) * -1
        print(i)
        while i <= math.floor(Range/2):
            self.pn1[i + 14] = (255, 0, 0, 0)
            self.pn1[i + 44] = (255, 0, 0, 0)
            i = i + 1 
        self.pn1.write()
        time.sleep_ms(500)
        
        j = Range * -1
        print(j)
        while j <= Range:
            self.pn1[j + 14] = (255, 0, 0, 0)
            self.pn1[j + 44] = (255, 0, 0, 0)
            j = j + 1
            
        self.pn1.write()
        
              
    def BrakeBlink(self):
        z = 0
        y = 0
        while y <= 5:
            x = Range * -1
            while x <= Range:
                if z == 0:
                    self.pn1[x + 14] = (255, 0, 0, 0)
                    self.pn1[x + 44] = (255, 0, 0, 0)
                    z = 1
                else:
                    self.pn1[x + 14] = (100, 0, 0, 0)
                    self.pn1[x + 44] = (100, 0, 0, 0)
                    z = 0
                self.pn1.write()
                x = x + 1
            y = y + 1
            time.sleep_ms(500)
            
        x = Range * -1
        while x <= Range:
            self.pn1[x + 14] = (255,0,0,0)
            self.pn1[x + 44] = (255,0,0,0)
            x = x + 1
        self.pn1.write()
        
    
    def BrakeFade(self):
        y = 10

        while y <= 255:
            x = Range * -1
            while x <= Range:
                self.pn1[x + 14] = (y, 0, 0, 0)
                self.pn1[x + 44] = (y, 0, 0, 0)
                x = x + 1
            self.pn1.write()
            y = y + 15
            print(y)
            time.sleep_ms(70)
            
            
            
    
    def DrivePulse(self):
        
        self.pn1[14 - Range] = (0, 0, 0, 0)
        self.pn1[14 + Range] = (0, 0, 0, 0)
        
        self.pn1[44 - Range] = (0, 0, 0, 0)
        self.pn1[44 + Range] = (0, 0, 0, 0)
        self.pn1.write()
        
        time.sleep_ms(500)
        
        self.pn1[14 - math.floor(Range / 2)] = (0, 0, 0, 0)
        self.pn1[14 + math.floor(Range / 2)] = (0, 0, 0, 0)
        
        self.pn1[44 - math.floor(Range / 2)] = (0, 0, 0, 0)
        self.pn1[44 + math.floor(Range / 2)] = (0, 0, 0, 0)
        self.pn1.write()
        
        time.sleep_ms(500)
        
        self.pn1[14] = (0, 0, 0, 0)
        
        self.pn1[44] = (0, 0, 0, 0)
        self.pn1.write()
        
        
    def DriveFade(self):
        y = 255

        while y >= 0:
            x = Range * -1
            while x <= Range:
                self.pn1[x + 14] = (y, 0, 0, 0)
                self.pn1[x + 44] = (y, 0, 0, 0)
                x = x + 1
            self.pn1.write()
            y = y - 15
            print(y)
            time.sleep_ms(50)
            
            
    def DriveBlink(self):
        z = 0
        y = 0
        while y <= 5:
            x = Range * -1
            while x <= Range:
                if z == 0:
                    self.pn1[x + 14] = (0, 100, 0, 0)
                    self.pn1[x + 44] = (0, 100, 0, 0)
                    z = 1
                else:
                    self.pn1[x + 14] = (0, 50, 0, 0)
                    self.pn1[x + 44] = (0, 50, 0, 0)
                    z = 0
                self.pn1.write()
                x = x + 1
            y = y + 1
            time.sleep_ms(500)
            
        x = Range * -1
        while x <= Range:
            self.pn1[x + 14] = (0,0,0,0)
            self.pn1[x + 44] = (0,0,0,0)
            x = x + 1
        self.pn1.write()