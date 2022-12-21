from machine import RTC
from machine import Pin
import time
rtc = RTC()
CLK = Pin(25, Pin.OUT)
fecha2 = rtc.datetime()
print(fecha2)
h = input("Ingresela hora: ")
m = input("Ingrese el minuto: ")

led = 0
while led < 478:
    fecha = rtc.datetime()
    if (fecha[4] == int(h) and fecha[5] == int(m)):
        CLK.value(1)
        #print(CLK.value())
        time.sleep_ms(250)
        CLK.value(0)
        #print(CLK.value())
        time.sleep_ms(250)
        led = led + 1


            


        
        
        
    
        
    
