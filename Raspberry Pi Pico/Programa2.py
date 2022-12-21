from machine import Pin
import time
pLED1 = Pin(25, Pin.OUT)    # create output pin on GPIO0
pLED2 = Pin(2, Pin.OUT)
pLED3 = Pin(3, Pin.OUT)
pLED4 = Pin(4, Pin.OUT)
Bott = Pin(5, Pin.IN, Pin.PULL_DOWN)
print(""+str(Bott.value()))
l1 = 1
l2 = 0
l3 = 0
l4 = 0
while True:
    if Bott.value():
        pLED1.value(l1)
        pLED2.value(l2)
        pLED3.value(l3)
        pLED4.value(l4)
        if l1 == 1:
            l1 = 0
            l2 = 1
            l3 = 0
            l4 = 0
        elif l2 == 1:
            l1 = 0
            l2 = 0
            l3 = 1
            l4 = 0
        elif l3 == 1:
            l1 = 0
            l2 = 0
            l3 = 0
            l4 = 1
        elif l4 == 1:
            l1 = 1
            l2 = 0
            l3 = 0
            l4 = 0
    time.sleep_ms(250) 
            
            
            
