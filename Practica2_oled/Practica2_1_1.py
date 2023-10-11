#librerías y módulos
import machine
import ssd1306

#comunicación y configuración de pines en la pantalla oled
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
displayOled = ssd1306.SSD1306_I2C(128, 64, i2c)

#Despliegue en pantalla oled
displayOled.fill(0) #propiedades para el despliegue
displayOled.show()
displayOled.text("Hola mundo", 0, 0) #escribir texto en la pantalla
displayOled.show() #mostrar texto
