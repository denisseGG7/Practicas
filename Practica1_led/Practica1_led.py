from machine import Pin
from utime import sleep

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()
    sleep(0.5)