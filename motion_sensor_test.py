from machine import Pin
from time import sleep
import turret_sound

POWER_PIN = Pin(2, Pin.OUT)
PIR_sensor = Pin(1, Pin.IN, Pin.PULL_UP)
POWER_PIN.high()
sleep(3)

LED = Pin(13, Pin.OUT)


while True:
   #print(PIR_sensor.value())
   if PIR_sensor.value() == 0:
       #print("NO Motion Detected! -> ")
       LED.high()
       sleep(.1)
   else:
       #print(" motion detected -> POWER_PIN is ON!!!!")
       #turret_sound.play("i_see_you")
       LED.low()
       sleep(2)
