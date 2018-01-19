#!/usr/bin/python
import time, RPi.GPIO as GPIO
from time import sleep
trigger = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.IN)
while True:
  i = GPIO.input(trigger)
  print('pin is: ' + str(i))
  sleep(0.1)

GPIO.cleanup()
