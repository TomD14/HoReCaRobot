from tof_i2c import TOF10120
from machine import Pin, Signal
from neopixel import NeoPixel

import time

# docs here : https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

tof=TOF10120()
alarm_led=Pin(22,Pin.OUT)
alarm = Signal(alarm_led, invert=True)

# collision detect warning light
class WarningBar:

    def __init__(self): # dit is de constructor, wordt uitgevoerd tijdens object creatie
            self.size = 30
            self.p = Pin(15)
            self.pn = NeoPixel(self.p,30,bpp=4)

    def off(self):
        for p in range(self.pn.n):
            # print(p)
            self.pn[p] = (0,0,0,0)
        self.pn.write()
        
    def red_bar(self, number):
        # we beginnen bij led0 .. verder
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if number > i:
                self.pn[p] = (255,0,0,0)
            else:
                self.pn[p] = (0,32,0,0)
            i = i+1
            
        self.pn.write()
    
    def green_bar(self, intensity):
        for p in range(self.pn.n):
            self.pn[p] = (0, intensity,0,0)
            # if number > i:
            #     self.pn[p] = (255,0,0,0)
            # else:
            #     self.pn[p] = (0,32,0,0)
            # i = i+1
        self.pn.write()

if __name__ == '__main__':

    wb = WarningBar()

    while True:
        time.sleep_ms(100)
        distance = tof.get_distance_filtered()
        print(distance)
        if distance > 1999:
            # nothing to see
            # all lights off
            wb.off()
            alarm.off() # inverted
        elif distance < 1999 and distance > 1000:
            # green bar intensity
            intensity = int ((2000 - distance) / (1000/30) )
            wb.green_bar(intensity)
            alarm.off()
        # elif distance > 1000:
            # safe
            # set all leds to green
         #   wb.off()
         #   alarm.off() # inverted
            
        elif distance < 1001:
            # number of bars...
            # 30 LED over 1000 mm
            # function => input=0 => alle 30 leds aan, input=100 => 1 led aan
            if distance > 0:
                # prevent div by zero
                num_leds = int(30 - (distance / (1000/30)))
            else:
                num_leds = 30
            
            print(num_leds)
            alarm.value((distance < 300))
            wb.red_bar(num_leds)            
                
                
            
            
