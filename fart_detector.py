#!/usr/bin/python
import time, RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
trigger = 4
fart = 0
wait_time = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.IN)

def detect_fart(trigger):
    fart = 0
    print "Engaging fart detection"
    print "Actively monitoring for farts"
    while True:
      i = GPIO.input(trigger)
      if i == 1:
        print "Fart Detected!"
        fart = 1
        break
      sleep(0.1)
    return fart

def clear_the_air(wait_time):
    for i in range(wait_time):
        time_left = wait_time - i
        print "Waiting for " + str(time_left) + " seconds, for the air to clear!"
        sleep(1)

while True:
    fart = detect_fart(trigger)
    if fart == 1:
        clear_the_air(wait_time)
