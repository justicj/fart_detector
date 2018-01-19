#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
from time import sleep
import os
trigger = 4
fart = 0
wait_time = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.IN)


def detect_fart(trigger):
    fart = 0
    clean_up = os.system("clear")
    print "Engaging fart detection"
    sleep(0.75)
    clean_up = os.system("clear")
    print "Engaging fart detection."
    sleep(0.75)
    clean_up = os.system("clear")
    print "Engaging fart detection.."
    sleep(0.75)
    clean_up = os.system("clear")
    print "Engaging fart detection..."
    print "Actively monitoring for farts"
    while True:
        i = GPIO.input(trigger)
        if i == 1:
            print "Fart Detected!"
	    print "¯\_(ツ)_/¯"
            fart = 1
            sleep(0)
            break
        sleep(0.1)
    return fart


def clear_the_air(wait_time):
    from pygame import mixer    
    mixer.init()
    mixer.music.load("evacuate.mp3")
    for i in range(wait_time):
        time_left = wait_time - i
        print 'Waiting ' + str(time_left) + ' seconds for the air to clear!'
	mixer.music.play(1)
	sleep(1)
        clean_up = os.system("clear")
        print "Fart Detected!"
	print "¯\_(ツ)_/¯"
    mixer.music.stop()

while True:
    fart = detect_fart(trigger)
    if fart == 1:
        clear_the_air(wait_time)

GPIO.cleanup()
