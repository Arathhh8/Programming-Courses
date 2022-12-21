import machine, onewire, ds18x20, time, framebuf
from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C

pir = Pin(0, Pin.IN)
led = Pin(3, Pin.OUT)
upA = Pin(15, Pin.IN, Pin.PULL_DOWN)
led.value(0)
sensor = 0
n = 0
d = 0
ancho=128
alto=64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
pantalla=SSD1306_I2C(ancho,alto,i2c)
pantalla.fill(0)  #Borra pantalla

timer = Timer() #Poner por default
# 
def sub_int_timer(timer):
    global n, sensor
    if sensor == 1:
        n = n+1
    if n >= 3 and d == 0:
        led.toggle()
        
timer.init(freq=1, mode=Timer.PERIODIC, callback=sub_int_timer) 
# #timer.init(freq=1, mode=Timer.ONE_SHOT, callback=sub_int_timer) 

def pir_int(pinx):
    global sensor
    print("Movimiento detectado")
    sensor = 1
        
    
pir.irq(trigger=Pin.IRQ_FALLING, handler=pir_int)
        
while True:
    if (n < 3 and upA.value()):
        pantalla.text("Alarma",40,20)
        pantalla.text("Desactivada", 25,35)
        pantalla.show()
        d = 1
            
    elif n >= 3 and d == 0:
        pantalla.text("ALERTA", 40,20)
        pantalla.show()

    


