from machine import Pin,Timer, PWM
import utime
import sg90
from neopixel import Neopixel
import turret_sound

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
#laser_1
laser_1 = PWM(Pin(13))
laser_1.freq(1000)
#Laser 2
laser_2 = PWM(Pin(27))
laser_2.freq(1000)

sg90.servo_pin(28)

debounce_ms = 2000
last_button_pressed_time = utime.ticks_ms()
print("last button pressed time initial=" + str(last_button_pressed_time))

def light_eye():
    brightness = 35
    for pixel_index in range(0,8):
            strip.set_pixel(pixel_index,(255,0,0),brightness)
            strip.show()


def fire():
  for i in range(20):
      laser_1.duty_u16(4555)
      laser_2.duty_u16(4555)
      utime.sleep_ms(60)
      laser_1.duty_u16(0)
      laser_2.duty_u16(0)
      utime.sleep_ms(60)
      
def start_firing():
    if is_closing == False and closed_flag == False:
        fire()
    
    
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
    print("opening")
    global closed_flag, is_closing
    turret_sound.play("i_see_you")
    utime.sleep_ms(2200)
    sg90.move_to(0)
    utime.sleep_ms(1200)
    stop()
    closed_flag = False
    is_closing = False

def button_pressed():
    global pressed, is_closing
    global closed_flag
    print("button pressed()")
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
    print(time_since_last_button_press)
    if (time_since_last_button_press > debounce_ms):
        pressed = True
        print("setting pressed to true")
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
      print("button pressed()")
      stop()
      closed_flag = True
  if closed_flag:
      utime.sleep_ms(1000)
      open()
      pressed = False
  else:
      start_firing()
      utime.sleep_ms(1000)
      laser_1.duty_u16(0)
      laser_2.duty_u16(0)
      close()

