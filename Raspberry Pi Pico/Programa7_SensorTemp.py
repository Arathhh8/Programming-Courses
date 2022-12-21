import machine, onewire, ds18x20, time, framebuf
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C

upA = Pin(15, Pin.IN, Pin.PULL_DOWN)
downA = Pin(14, Pin.IN, Pin.PULL_DOWN)
upB = Pin(13, Pin.IN, Pin.PULL_DOWN)
downB = Pin(12, Pin.IN, Pin.PULL_DOWN)
LED = Pin(18, Pin.OUT)
baja = 21
alta = 21
ancho=128
alto=64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
pantalla=SSD1306_I2C(ancho,alto,i2c)

pantalla.fill(0)  #Borra pantalla
time.sleep(1)

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
act = 0
 
while True:
    if upA.value():
        alta = alta + 1
        print("Alta: "+str(alta))
    elif downA.value():
        alta = alta - 1
        print("Baja: "+str(alta))
    elif upB.value():
        baja = baja + 1
        print("Baja: "+str(baja))
    elif downB.value():
        baja = baja - 1
        print("Baja: "+str(baja))
    if ds_sensor.read_temp(roms[0]) < baja:
        LED.value(0)
    elif ds_sensor.read_temp(roms[0]) > alta:
        LED.value(1)
    pantalla.text("Temperatura",0,0)
    pantalla.text("Alta: "+str(alta),0,15)
    pantalla.text("Baja: "+str(baja),0,25)
    pantalla.text("Actual: ",0,45)
    pantalla.show()
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    print(ds_sensor.read_temp(roms[0]))
    pantalla.text(str(ds_sensor.read_temp(roms[0])),58,45)
    pantalla.show()
    time.sleep(0.5)
    pantalla.fill(0)
     
   