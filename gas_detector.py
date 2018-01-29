#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
from time import sleep
import os
from pygame import mixer
trigger = 4
gas = 0
wait_time = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.IN)


def detect_gas(trigger):
    gas = 0
    clean_up = os.system("clear")
    print "Engaging gas detection"
    sleep(0.75)
    clean_up = os.system("clear")
    print "Engaging gas detection."
    sleep(0.75)
    clean_up = os.system("clear")
    print "Engaging gas detection.."
    sleep(0.75)
    clean_up = os.system("clear")
    print "Engaging gas detection..."
    print "Actively monitoring for gas"
    while True:
        i = GPIO.input(trigger)
        if i == 1:
            print "Gas Detected!"
	    print "¯\_(ツ)_/¯"
            gas = 1
            sleep(0)
            break
        sleep(0.1)
    return gas


def clear_the_air(wait_time):  
    mixer.init()
    mixer.music.load("evacuate.mp3")
    for i in range(wait_time):
        time_left = wait_time - i
        print 'Waiting ' + str(time_left) + ' seconds for the air to clear!'
	mixer.music.play(1)
	#placeholder for led on
	sleep(1)
	#placeholder for led off
        clean_up = os.system("clear")
        print "Gas Detected!"
	print "¯\_(ツ)_/¯"
    mixer.music.stop()

while True:
    gas = detect_gas(trigger)
    if gas == 1:
        clear_the_air(wait_time)

GPIO.cleanup()
