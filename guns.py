from machine import Pin,Timer, PWM
import utime
import turret_sound


class Guns:

    PWM_FREQUENCY = 1000
    left_gun = None
    right_gun = None

    def __init__(self, left_pin, right_pin):
        self.left_gun = PWM(Pin(left_pin))
        self.right_gun = PWM(Pin(right_pin))
        self.left_gun.freq(self.PWM_FREQUENCY)
        self.right_gun.freq(self.PWM_FREQUENCY)


    def fire(self):
        for i in range(20):
            self.left_gun.duty_u16(4555)
            self.right_gun.duty_u16(4555)
            utime.sleep_ms(60)
            self.left_gun.duty_u16(0)
            self.right_gun.duty_u16(0)
            utime.sleep_ms(60)
            
    
