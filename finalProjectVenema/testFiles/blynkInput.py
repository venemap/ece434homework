#!/usr/bin/env python3
# From: https://github.com/blynkkk/lib-python
# Blink the USR3 LED in response to a V0 input.
import blynklib, os, sys, smbus, math, schedule, time
import Adafruit_BBIO.GPIO as GPIO

# Setup the LED
LED = 'USR3'
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1) 
alarmSet = 0 
a = 0


# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH', default="")
BLYNK_AUTH = "LrwqMOl2bfhoo7EKqAhx-0ahGRge92r_"
if(BLYNK_AUTH == ""):
    print("BLYNK_AUTH is not set")
    sys.exit()

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V0')
def my_write_handler(pin, value):
    global alarmSet, a
    print("v0 write")
    timeInSeconds = int(value[0])
    hours = math.floor(timeInSeconds/3600)
    minutes = math.floor((timeInSeconds - hours*3600)/60)
    seconds = timeInSeconds - hours*3600 - minutes*60
    timeString = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    if len(str(seconds))==1:
        seconds = "0" + str(seconds)
    secondsString = ":" + str(seconds)
    
    print(secondsString)
    if(alarmSet):
        schedule.cancel_job(a)
    a = schedule.every().minute.at(secondsString).do(job)
    alarmSet = 1
    print(timeString)
    
    

# This is a non-blocking event #
#GPIO.add_event_detect(button, GPIO.BOTH, callback=pushed) 
def job():
    print("doing job")


while True:
    blynk.run()
    if(alarmSet):
        schedule.run_pending()
    time.sleep(1)
    print(a)
    
