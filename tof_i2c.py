
# Time of Flight sensor TF10120 via i2c (serial not used)
# Door Edwin van den Oetelaar op een zondag ochtend 23/10/2022
# voor Tom en RIGS robot Fontys, kan als CLIFF sensor gebruikt worden
# CLIFF sensor meet grond afstand en ziet val-kuilen en gaten
# MicroPython v1.19.1 on 2022-10-14; ESP32 module
# info : micropython.org
#
# ESP32 met TOF10120 op i2c pins 
# 2 == i2c data pin
# 4 == i2c clock pin
# de blinky LED zit op pin 22 (anode=vcc, pull down NMOS style => inverted)
# de LED strip WS2813 RGBW zit op pin 15 via level converter
# editor is Thonny.org
# filename : tof_i2c.py
# usage :
# import tof_i2c
# tof1 = tof_i2c.TOF1020()

# 2.4.4 I2C
# 1. Parameter and data register addresses (vertaald uit Chinese datasheet)
# Address   | Data/parameter          | Number of bytes | Read/write | Unit Data | form     | Value range
# --------------------------------------------------------------------------------------------------------------------------------------------------
# 0x00-0x01 | Real-time distance      | 2               | read-only  | mm        | Hex code | 100mm-1800mm
# 0x04-0x05 | Filter distance         | 2               | read-only  | mm        | Hex code | 100mm-1800mm
# 0x06-0x07 | Distance deviation      | 2               | read/write | mm        | Hex code | signed number -99mm-99mm
# 0x08      | Distance data mode      | 1               | read/write | ---       | Hex code | 0 - Filtered values, 1 - Real time value
# 0x09      | Distance sending mode   | 1               | read/write | ---       | Hex code | 0 - Module send (serial), 1 - Host read (serial, i2c)
# 0x0c-0x0d | Max. measuring distance | 2               | Read only  | mm        | Hex code | 100mm-1800mm
# 0x0f      | I2C slave address       | 1               | read/write | ---       | Hex code | 0x02~0xfe, bit7~bit1 valid bit0=0

# todo: queue, alarm bij cliff en background thread

from machine import Pin
from machine import I2C
import time  # delay
import struct  # unpack binary data

DEBUG = False  # flag verbose logging


class TOF10120:
    """
        Werkt docstring ook in micropython?
        We kunnen meer dan 1 TOF sensor op de bus hebben, default is de id==82
        De conversie duurt max 33 ms (dus 30 metingen per seconde)
    """

    def __init__(self, dev_id=82):
        """
            dit is de constructor, wordt uitgevoerd tijdens object creatie
            default setup van I2C op hardware
            check aanwezigheid van device op bus
        """
        self.sda = Pin(2)  # i2c data pin
        self.scl = Pin(4)  # i2c clock pin
        # activate hardware interface 0 , map pins, set speed
        self.i2c = I2C(0, scl=self.scl, sda=self.sda, freq=400000)
        # make list of all i2c devices on the bus
        sr = self.i2c.scan()
        if DEBUG: print(f'i2c scan gives {sr}')
        # if device we need is not on bus stop right here
        assert dev_id in sr, f"dev_id={dev_id} not found on bus"
        # store device id in object instance for later use
        self.dev_id = dev_id

    def get_distance(self, register=0x00) -> int:
        # local buffer 2 bytes size to store data
        buffer = bytearray(2)
        # read register at 0x00 realtime distance, 2 bytes
        if DEBUG: print(register)
        result = self.i2c.readfrom_mem_into(self.dev_id, register, buffer)
        # unpack 2 bytes into 1 short integer using library function
        # read docs about packing/unpacking +big endian and little endian +network alignment
        # this is an important concept that must be fully understood !!
        distance = struct.unpack('>H', buffer)
        # alternative without lib function : distance = 256 * buffer[1] + buffer[0]
        
        if DEBUG: d2=buffer[0] * 256 + buffer[1] ; print(f'distance={distance} == {d2}')
        return distance[0] # first element of the tuple only

    def get_distance_filtered(self) -> int:
        # no data on exact low pass filter function
        # results show low pass result, could be average over 10 latest samples
        # real data is missing
        return self.get_distance(register=0x04)  # see table
    
    def get_max_distance(self) -> int:
        return self.get_distance(register=0x0C) # see table
    
    def set_alt_i2c_address(self, current_address, new_address):
        # NB datasheet gaat uit van 8 bit adressen (bit 0 is R/W) en wij van 7 bit 
        # we shiften de adressen dus 1 bit naar links
        # check dit zelf svp, zoek op 7 bit vs 8 bit i2c
        assert 127 > current_address > 1
        assert 127 > new_address > 1
        # check current address
        buf = bytearray(1)  # buffer to store data into
        self.i2c.readfrom_mem_into(current_address, 0x0F, buf)
        if DEBUG: print(buf[0])  # returns 164, but our i2c is 82... what gives?
        buf[0] = new_address << 1  # fix address
        # store byte 'new_address' at location 0x0f of device at current_address
        self.i2c.writeto_mem(current_address, 0x0F, buf)
        # the device now has a new i2c device_id on the bus and communication will fail

    def run_test(self, n=100):
        # run n number of times, or forever when n==0
        i = n
        while (i > 0 or n == 0):
            dist_in_mm = self.get_distance()
            dist_in_mm_filtered = self.get_distance_filtered()
            print(f'd={dist_in_mm} mm  d_filter={dist_in_mm_filtered} mm')
            time.sleep_ms(33)
            i = i - 1


if __name__ == '__main__':
    # self test
    DEBUG = False  # no verbose logging
    k = TOF10120(dev_id=82)
    print(k.get_max_distance())
    # k.set_alt_i2c_address(83,82)
    k.run_test(0)  # 0=run_forever
