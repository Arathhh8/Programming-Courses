import machine, onewire, ds18x20, time, framebuf
from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C


ancho=128
alto=64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
pantalla=SSD1306_I2C(ancho,alto,i2c)
pantalla.fill(0)  #Borra pantalla

n = 0
s = 0
d = 0
i = 0
timer = Timer() #Poner por default

def sub_int_timer(timer):
    global  s, n, d, i
    s = s+1
    n = n+1
    

timer.init(freq=1, mode=Timer.PERIODIC, callback=sub_int_timer) 
#timer.init(freq=1, mode=Timer.ONE_SHOT, callback=sub_int_timer) 

while True:
    if s == 2:
        print(str(i))
        i = i + 55
        pantalla.text("___",148-i,20)
        pantalla.show()
        if i > 100:
            i = 0
           
    if s == 4:
        d = d + 56
        pantalla.text("___",121-d,40)
        pantalla.show()
        if d > 100:
            d = 0
        s = 0
        
    if n == 8:
        pantalla.fill(0)
 
        
    pass