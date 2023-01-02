#In order ror this example-code to work, make sure you have a
#card with at least one folder, containing at least two mp3:s.
#The folders should be named 01, 02 etc and files should be named
#001.mp3, 002.mp3 etc.
from utime import sleep_ms, sleep
from picodfplayer import DFPlayer
import random

DEBUG = False
#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE=0
TX_PIN = 12
RX_PIN=13
BUSY_PIN=6

FIRE = "fire"
FIRING = "firing"
PRODUCT = "product"
IS_ANYONE_THERE = "is_anyone_there"
HELLO = "hello"
ARE_YOU_STILL_THERE = "are_you_still_there"
COME_OVER_HERE = "come_over_here"
WHOS_THERE = "whos_there"
SEARCHING = "searching"

THERE_YOU_ARE = "there_you_are"
I_SEE_YOU = "i_see_you"
CAN_I_HELP_YOU = "can_i_help_you"
TARGET_LOST = "target_lost"
TARGET_ACQUIRED = "target_acquired"
HI = "hi"

dispensing_product = {"folder":1,"track":3}
hi = {"folder":1, "track":1 }
target_acquired = {"folder":1,"track":2}
firing = {"folder":1,"track":4}
there_you_are = {"folder":1,"track":7}
i_see_you = {"folder":1,"track":8}
activated = {"folder":3,"track":1}
whos_there = {"folder":3,"track":3}
deploying = {"folder":3,"track":5}
preparing_dispense_product = {"folder":3,"track":6}
shutting_down = {"folder":4,"track":2}
put_me_down = {"folder":5,"track":1}
please_put_me_down = {"folder":5,"track":6}
help = {"folder":5,"track":7}
good_night = {"folder":6,"track":2}
sleep_mode_activated = {"folder":6,"track":6}
come_over_here = {"folder":7,"track":1}
are_you_still_there = {"folder":7,"track":2}
target_lost = {"folder":7,"track":3}
can_i_help_you = {"folder":7,"track":4}
searching = {"folder":7,"track":5}
hello = {"folder":7,"track":6}
sentry_mode = {"folder":7,"track":9}
is_anyone_there = {"folder":7,"track":10}
malfunctioning = {"folder":8,"track":1}
ow_ow_ow = {"folder":8,"track":3}
fire1 = {"folder":9,"track":5}
fire2 = {"folder":9,"track":6}
fire3 = {"folder":9,"track":7}
fire = {"folder":9,"track":8}
alert = {"folder":9,"track":13}
deploy_arms = {"folder":9,"track":1}
retract_arms = {"folder":9,"track":4}


sound_map = {PRODUCT:dispensing_product, HI:hi, TARGET_ACQUIRED: target_acquired, FIRING:firing,
             THERE_YOU_ARE:there_you_are, I_SEE_YOU:i_see_you, "activated":activated,
             WHOS_THERE:whos_there, "deploying":deploying, "preparing_dispense_product":preparing_dispense_product,
             "shutting_down":shutting_down, FIRE:fire, ARE_YOU_STILL_THERE: are_you_still_there, IS_ANYONE_THERE:is_anyone_there,
             HELLO:hello, TARGET_LOST:target_lost, SEARCHING: searching, COME_OVER_HERE:come_over_here,
             CAN_I_HELP_YOU:can_i_help_you, HELLO:hello}

searching_for_target = [IS_ANYONE_THERE, COME_OVER_HERE, SEARCHING]

target_lost = [ARE_YOU_STILL_THERE, TARGET_LOST, HELLO]

target_spotted = [I_SEE_YOU, CAN_I_HELP_YOU, THERE_YOU_ARE, WHOS_THERE, TARGET_ACQUIRED]

#Create player instance
player=DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)


#Check if player is busy.
if (DEBUG):
    print('Playing?', player.queryBusy())
#Play the first song (001.mp3) from the first folder (01)

def play(key):
    if (DEBUG):
        print("playing sound", key)
    folder = sound_map[key]["folder"]
    track = sound_map[key]["track"]
    if (DEBUG):
        print("folder=" + str(folder) + " track=" + str(track))
    player.playTrack(folder, track)

def target_spotted():
    random_spotted_phrase = random.choice(target_spotted)
    play(random_spotted_phrase)

def target_lost():
    random_lost_phrase = random.choice(target_lost)
    play(random_lost_phrase)

def target_search():
    random_search_phrase = random.choice(searching_for_target)
    play(random_search_phrase)

if __name__=="__main__":
    play("product")
    sleep(3)

    play("fire")
    sleep(1)

    play("are_you_still_there")
    sleep(1)


