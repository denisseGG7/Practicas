# Practica 2.1 Hola mundo y la Hora de internet

## 2.1.1 Práctica de inicio: Desplegar algo en pantalla, algunos quieren el logo de ISC, esta bien, otro texto simple en el OLED DIsplay
### Código Micropython
_En este apartado se presenta el código .py para desplegar **Hola mundo**_
```python
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
```

### Conexión simulada
_Utilizando el software de Wokwi se simulo la conexión en el Raspberry Pico W_
![](ConexionSimulada.png)

### Conexión física
_Usando como ejemplo la conexión simulada, se hizo el circuito de forma física_ 
![](ConexionFisica.png)
![](HolaM.png)

## 2.1.2 Desplegar la hora de Internet usando Wi-Fi integrada para que interrogue un servidor NTP Time Server, en el OLED DIsplay
### Código Micropython
_En este apartado se presenta el código .py para desplegar **hora de internet**_
```python

```
### Conexión simulada
_Utilizando el software de Wokwi se simulo la conexión en el Raspberry Pico W_
![]()

### Conexión física
_Usando como ejemplo la conexión simulada, se hizo el circuito de forma física_ 
![]()
