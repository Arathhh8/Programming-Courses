from machine import Pin, Timer

led1 = Pin(3, Pin.OUT)
n = 0
s = 1
upA = Pin(15, Pin.IN, Pin.PULL_DOWN)
downA = Pin(14, Pin.IN, Pin.PULL_DOWN)
timer = Timer() #Poner por default

def sub_int_timer(timer):
    global led1, s, n
    if s == 1:
        n = n+1
        if n == 5:
            led1.value(0)
            s = 0
            n = 0

timer.init(freq=1, mode=Timer.PERIODIC, callback=sub_int_timer) 
#timer.init(freq=1, mode=Timer.ONE_SHOT, callback=sub_int_timer) 

while True:
    if upA.value():
        led1.value(1)
        s = 1
    if  downA.value():
        led1.value(1)
        s = 1
        
    pass
    

    