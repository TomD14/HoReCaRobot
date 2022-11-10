from machine import Pin
from neopixel import NeoPixel
from time import sleep


class LightDir:
    
    def __init__(self): # dit is de constructor, wordt uitgevoerd tijdens object creatie
            self.size = 30
            self.p = Pin(15)
            self.pn = NeoPixel(self.p,30,bpp=4)

    def Left(self):
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if 5 > i:
                self.pn[p] = (255,0,0,0)
            else:
                self.pn[p] = (0,32,0,0)
            i = i+1
            
        self.pn.write()
        
    def Front(self):
        i = 0 # teller hoeveel leds al actief zijn
        for p in range(self.pn.n):
            if i < 5:
                self.pn[p] = (0,32,0,0)
            elif i > 5 and i < 10:
                self.pn[p] = (255,0,0,0)
            else:
                self.pn[p] = (0,32,0,0)
                
        i = i+1
        self.pn.write()
        
    def off(self):
        for p in range(self.pn.n):
            # print(p)
            self.pn[p] = (0,0,0,0)
        self.pn.write()
        
    def web_page(self):
              html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
      h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
      border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
      .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
      <p><a href="/?NeoLeft"><button class="button">Left</button></a></p>
      <p><a href="/?NeoFront"><button class="button">Front</button></a></p>
      <p><a href="/?NeoOff"><button class="button button2">OFF</button></a></p></body></html>"""
              return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
    
    
    
if __name__ == '__main__':

    LD = LightDir()

    while True:
        
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        Left = request.find('/?NeoLeft')
        Off = request.find('/?NeoOff')
        Front = request.find('/?NeoFront')
        if Left == 6:
            LD.Left()
            print('Left')
        if Off == 6:
            LD.off()
            print('off')
        if Front == 6:
            LD.Front()
            print('Front')
        response = LD.web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()