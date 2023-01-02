#In order ror this example-code to work, make sure you have a
#card with at least one folder, containing at least two mp3:s.
#The folders should be named 01, 02 etc and files should be named
#001.mp3, 002.mp3 etc.
from utime import sleep_ms, sleep
from picodfplayer import DFPlayer

DEBUG = False
#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE=0
TX_PIN = 12
RX_PIN=13
BUSY_PIN=6

IS_ANYONE_THERE = "is_anyone_there"
HELLO = "hello"
ARE_YOU_STILL_THERE = "are_you_still_there"
COME_OVER_HERE = "come_over_here"
WHOS_THERE = "whos_there"

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


sound_map = {"product":dispensing_product, "hi":hi, "target_acquired": target_acquired, "firing":firing,
             "there_you_are":there_you_are, "i_see_you":i_see_you, "activated":activated,
             "whos_there":whos_there, "deploying":deploying, "preparing_dispense_product":preparing_dispense_product,
             "shutting_down":shutting_down, "fire":fire, "are_you_still_there": are_you_still_there}

searching_key_sound_collection = ["is_anyone_there"]

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

def random_search():
    print("play random sound dealing with searching")

if __name__=="__main__":
    play("product")
    sleep(3)

    play("fire")
    sleep(1)

    play("are_you_still_there")
    sleep(1)


