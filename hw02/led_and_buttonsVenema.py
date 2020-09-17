#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO   
import time

btn1 = "P9_18" #led output
btn2 = "P9_24" 
btn3 = "P9_26"
btn4 = "P9_30"

btnRight = "P9_13" 
btnUp = "P9_11"
btnLeft = "P9_17"
btnDown = "P9_12"

def btn1callback(channel):
    state = GPIO.input(channel)
    if state:
        GPIO.output(btn1, 1)
    else:
        GPIO.output(btn1, 0)  
        
def btn2callback(channel):
    state = GPIO.input(channel)
    if state:
        GPIO.output(btn2, 1)
    else:
        GPIO.output(btn2, 0)  
        
def btn3callback(channel):
    state = GPIO.input(channel)
    if state:
        GPIO.output(btn3, 1)
    else:
        GPIO.output(btn3, 0)  
        
def btn4callback(channel):
    state = GPIO.input(channel)
    if state:
        GPIO.output(btn4, 1)
    else:
        GPIO.output(btn4, 0)  

GPIO.setup(btnRight, GPIO.IN)
GPIO.setup(btnLeft, GPIO.IN)
GPIO.setup(btnUp, GPIO.IN)
GPIO.setup(btnDown, GPIO.IN)
GPIO.setup(btn1, GPIO.OUT)
GPIO.setup(btn2, GPIO.OUT)
GPIO.setup(btn3, GPIO.OUT)
GPIO.setup(btn4, GPIO.OUT)

GPIO.add_event_detect(btnRight, GPIO.BOTH)
GPIO.add_event_detect(btnLeft, GPIO.BOTH)
GPIO.add_event_detect(btnUp, GPIO.BOTH)
GPIO.add_event_detect(btnDown, GPIO.BOTH)

GPIO.add_event_callback(btnRight, btn1callback)
GPIO.add_event_callback(btnLeft, btn2callback)
GPIO.add_event_callback(btnUp, btn3callback)
GPIO.add_event_callback(btnDown, btn4callback)


print('Ready for LED Presses')
while True:
    time.sleep(0.1)

