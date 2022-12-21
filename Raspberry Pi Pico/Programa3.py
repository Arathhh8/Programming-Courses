from machine import Pin, PWM
import time

pwmLED = PWM(Pin(2))    # create output pin on GPIO0
pwmI = Pin(5, Pin.IN, Pin.PULL_DOWN)
pwmD = Pin(15, Pin.IN, Pin.PULL_DOWN)
pwmLED.freq(100)
pwmLED.duty_u16(0)
#print("Frecuencia = " +str(pwmLED.freq()))
#print(pwmLED.duty_u16())
ct =0
inc =3276
dec =3276
while ct<65536:
    pwmINC = str(pwmI.value())
    pwmDEC = str(pwmD.value())
    if (pwmINC == "1" and ct < 62260):
        ct = ct + inc
        pwmLED.duty_u16(ct)
        print("Ciclo de trabajo = " +str(pwmLED.duty_u16()))
    elif (pwmDEC == "1" and ct > 3274):
        ct = ct - dec
        pwmLED.duty_u16(ct)
        print("Ciclo de trabajo = " +str(pwmLED.duty_u16()))
    time.sleep_ms(150)
     #con 50ms el botón presenta rebotes 