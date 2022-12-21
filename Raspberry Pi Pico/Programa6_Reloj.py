from machine import RTC
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

ancho=128
alto=64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
pantalla=SSD1306_I2C(ancho,alto,i2c)
pantalla.fill(0)  #Borra pantalla
time.sleep(1)
rtc = RTC()
CLK = Pin(25, Pin.OUT)
while True:
    fecha2 = rtc.datetime()
    a = str(fecha2[0])
    mo = str(fecha2[1])
    d = str(fecha2[2])
    h = str(fecha2[4])
    m = str(fecha2[5])
    s = str(fecha2[6])
    pantalla.fill(0)
    pantalla.text(s,84,20)
    pantalla.text(h+":",40,20)
    pantalla.text(m+":",62,20)
    pantalla.text(d+"/"+mo+"/"+a,30,40)
    pantalla.show()
    time.sleep(1)

    
    
    
    
