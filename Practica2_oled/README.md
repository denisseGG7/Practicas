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

_Se desplegó el texto **Guipzot 20211788** para modificación del mensaje básico_
![](MensajeOled.png)

## 2.1.2 Desplegar la hora de Internet usando Wi-Fi integrada para que interrogue un servidor NTP Time Server, en el OLED DIsplay
### Código Micropython
_En este apartado se presenta el código .py para desplegar **hora de internet**_
```python
#librerias
import network
import urequests
import utime
from machine import Pin, I2C
import ssd1306

#bloque para la conexión a Wi-Fi
def conexion(ssid, contra):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("¡Espere! Conectando a Wi-Fi ")
        sta_if.active(True)
        sta_if.connect(ssid, contra)
        while not sta_if.isconnected():
            pass
    print("¡Conexión con éxito!")
    print('IP:', sta_if.ifconfig()[0])

def hr_internet():
    #obtención de la hora actual
    url = "http://worldtimeapi.org/api/ip"
    response = urequests.get(url)
    dat = response.json()
    return dat['datetime']

def config_pantalla():
    #configuración de pines para la conexión de la pantalla     
    i2c = I2C(0, sda=Pin(8), scl=Pin(9)) 
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    return oled


def despliegue_oled(oled, hr):
    #despliegue de resultados en pantalla
    oled.fill(0)
    oled.text("Hora (PST):", 0, 0)
    oled.text(hr, 0, 16)
    oled.show()

def main():
    ssid = "TecNM-ITT-Docentes 2"
    contra = "tecnm2022!"

    conexion(ssid, contra)
    oled = config_pantalla()

    while True:
        hr = hr_internet()
        print("Hora actual:", hr)
        despliegue_oled(oled, hr)
        utime.sleep(60)

if __name__ == '__main__':
    main()
```
### Resultados en consola
_Despliegue de resultados que se muestran en la consola del software de Thonny_
![]()

### Conexión física
_Realización del circuito de forma física_ 
![]()
