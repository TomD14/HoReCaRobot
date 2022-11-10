# looplicht knighrider style
# Door Edwin van den Oetelaar op een zaterdag middag
# test van NeoPixel ding voor Tom en RIGS robot
# op de ESP32 met NeoPixel op pin 15
# deze strip https://www.tinytronics.nl/shop/en/lighting/led-strips/led-strips/ws2813-digital-5050-rgbw-led-strip-30-leds-1m
# dit is een RGB+W strip dus 4 LEDS in 1 chipje
# de standaard blinky LED zit op pin 22 (pull down == inverted)
# code is MicroPython v1.19.1 on 2022-10-14; ESP32 module with ESP32
# micropython.org
# editor is Thonny.org
# filename : knightrider.py
# usage :
# import knightrider
# knightrider.run()
# todo: extra patronen en background thread

from machine import Pin
from neopixel import NeoPixel
import time

class KnightRider:
    """
        Werkt docstring ook in micropython
    """
    def __init__(self): # dit is de constructor, wordt uitgevoerd tijdens object creatie
        self.size = 30
        self.p = Pin(15)
        self.pn = NeoPixel(self.p,30,bpp=4)
        
    def _one_hot(self, i=None,arr=None,size=None, value=(255,0,0,0)):
        # help functie om 1 led in de strip rood/value te maken
        assert (i is not None), "index missing"
        assert (arr is not None), "np array missing"
        assert (size is not None), "size missing"
        
        # print(i,arr,size)
        
        for j in range(size):
            if i==j :
                arr[j] = value # 1 led aan ROOD full
            else:
                arr[j] = (0,0,0,0) # alles uit
        
    def run(self):
        """Run knightrider simulation on Neopixel strip"""
        
        kleurtjes = [ (255,0,0,0), (0,255,0,0), (0,0,255,0), (0,0,0,128) ]
        
        while True:
            
            for k in kleurtjes:
                    
                for i in range(self.size * 2):
                    # mirror index on end of light strip
                    if (i > self.size -1):
                        i = (2 * self.size ) - i # teruglopen van de index spiegel in lengte
                        
                    self._one_hot(i, self.pn, self.size, k)
                    
                    self.pn.write()         # output de hele array naar de strip
                    time.sleep_ms(30)      # sleep for 30 milliseconds
                
                    self.pn.write()
                
if __name__ == '__main__':
    # self test
    k=KnightRider()
    k.run()
    
        

