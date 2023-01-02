from machine import Pin,Timer, PWM
import utime
import sg90
from neopixel import Neopixel
import turret_sound
from guns import Guns

## Initialize Motion Sensor (HiLetgo AM312 Mini Pyroelectric PIR Human Sensor)
#PIR_POWER_PIN = Pin(2, Pin.OUT) # did not run this to the always on 3.3Volt line
#PIR_POWER_PIN.high() # need to always be powered on if want to sense.
pir_sensor = Pin(1, Pin.IN, Pin.PULL_UP)
person_detected = False

numpix = 8
strip = Neopixel(numpix, 0, 14, "GRB")

button = Pin(15, Pin.IN, Pin.PULL_DOWN)  # 13 number pin is input
led = Pin(25, Pin.OUT)
sg90.servo_pin(28)

closed_flag = True
pressed = False
irq_state = None
is_closing = False

## Init guns:
guns = Guns(13,27)

sg90.servo_pin(28)

debounce_ms = 2000
last_button_pressed_time = utime.ticks_ms()
print("last button pressed time initial=" + str(last_button_pressed_time))


def person_detected(pin):
    global person_detected
    person_detected = True
    #print("Detected!!!!!!!!!!!!!!!!!!!!!!!!!")
    
pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=person_detected)

def light_eye():
    brightness = 35
    for pixel_index in range(0,8):
            strip.set_pixel(pixel_index,(255,0,0),brightness)
            strip.show()
      
def start_firing():
    if is_closing == False and closed_flag == False:
        guns.fire()
    
    
def stop():
    sg90.move_to(90)

def close():
    global is_closing
    if is_closing == False:
        is_closing = True
        turret_sound.play("are_you_still_there")
        utime.sleep_ms(2000)
        sg90.move_to(95)

def open():
    #print("opening")
    global closed_flag, is_closing
    turret_sound.play("i_see_you")
    utime.sleep_ms(2200)
    sg90.move_to(0)
    utime.sleep_ms(1000)
    stop()
    closed_flag = False
    is_closing = False

def button_pressed():
    global pressed, is_closing
    global closed_flag
    #print("button pressed()")
    stop()
    closed_flag = True
    is_closing = False
    #irq_state = machine.disable_irq()
    # Timer(mode=Timer.ONE_SHOT, period=500,callback=debounce)
    #led.value(1)
    #utime.sleep_ms(500)
    #led.value(0)
    # machine.enable_irq(irq_state)
    #pressed = False
    
    
    
def button_handler(pin):
    global pressed
    global last_button_pressed_time
    current_time = utime.ticks_ms()
    time_since_last_button_press = utime.ticks_diff(current_time,last_button_pressed_time)
    #print(time_since_last_button_press)
    if (time_since_last_button_press > debounce_ms):
        pressed = True
        #print("setting pressed to true")
        last_button_pressed_time = current_time
  
   

#open()
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
#utime.sleep_ms(2000)

#close()
light_eye()

#turret_sound.play("are_you_still_there")

while True:
  
  #print("looping")
  if pressed:
      #print("button pressed()")
      stop()
      closed_flag = True
      #print("Detected", person_detected)
  
  if closed_flag and person_detected==True:
      utime.sleep_ms(1000)
      open()
      pressed = False
  elif closed_flag == False and person_detected==True:
      start_firing()
      person_detected = False
      utime.sleep_ms(1000)
  elif closed_flag == False and is_closing == False and person_detected == False:
      close()

