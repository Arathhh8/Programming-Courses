from machine import ADC, PWM, Pin
import time

PLED = PWM(Pin(25))
PLED.freq(100)
adc = ADC(Pin(26))

while True:
    valorADC = adc.read_u16()
    porc =  valorADC* 100 // 65535
    PLED.duty_u16(valorADC)
    print(f'Intensidad al {porc}%')
    time.sleep_ms(600)