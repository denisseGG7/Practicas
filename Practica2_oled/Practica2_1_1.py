#librerías
import machine
import ssd1306

#comunicación y configuración de pines
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
displayOled = ssd1306.SSD1306_I2C(128, 64, i2c)

displayOled.fill(0)
displayOled.show()
#Despliegue en pantalla oled
displayOled.text("Hola mundo", 0, 0)
displayOled.show()
