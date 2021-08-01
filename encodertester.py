# encoder tester
import RPi.gpio as GPIO
import time

Lencoder = 25
Rencoder = 8

GPIO.setup(Lencoder, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Rencoder, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
timer = time.time()
def encoder_callback():
    counter += 1

GPIO.add_event_detect(Lencoder, GPIO.RISING, callback=encoder_callback)

while True:
    if counter == 20:
        elapsed = time.time()-timer
        print("{} revs/s".format(1/elapsed))

