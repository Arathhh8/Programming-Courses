"""
Hay mas metodos que se pueden usar con esta libreria 
para graficos y efectos
Ver video con mas explicaciones
https://www.youtube.com/watch?v=H7kyZZcd1dM&t=58s
"""
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

ancho=128
alto=64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
pantalla=SSD1306_I2C(ancho,alto,i2c)

pantalla.fill(0)  #Borra pantalla
time.sleep(1)
#pantalla.fill(1) #llena con unos la pantalla

#Pantalla en pixeles 0,0   .....  128,0
#Pantalla en pixeles 0,64  .....  128,64

#Argumentos("texto",x,y)
pantalla.text("Hola Mundo",0,0)
pantalla.show()
time.sleep(2)
pantalla.text("Son las 4:22", 0,20)
pantalla.show()

#Se puede mandar una variable tambien
#Pero hay que chacer un casting a string
#de la variable
#Argumentos(str(variable),x,y)
# valor=50
# pantalla.text(str(valor),0,56)
# pantalla.show() #Metodo show para mostrar el texto