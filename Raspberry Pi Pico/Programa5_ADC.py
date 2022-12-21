from machine import ADC, Pin, PWM 
import time
PLED = PWM(Pin(25),)
PLED.freq(100)
adc = ADC(Pin(26))

while True:
    valorADC = adc.read_u16()
    print(valorADC*3.3/65535)        # read value, 0-65535 across voltage range 0.0v - 3.3v
    PLED.value(1)
    PLED.value(0)
    time.sleep(1)
    
