#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO   
import time, math
from os import system

pin = "P9_14" #led output
btnRight = "P9_13" 
btnUp = "P9_11"
btnLeft = "P9_17"
btnDown = "P9_12"
currXPos = 0
currYPos = 0

class screen:
    def __init__(self):
        self.size = 0
        self.matrix = {}
        self.x = 0
        self.y = 0
        
def printScreen(screenInfo):
    x = 0
    y = 0
    z = 0
    
    print('   ', end = '')
    for z in range(screenInfo.size):
        print(z, end = ' ') #top numbers
    print('')
    
    for x in range(screenInfo.size):
        print(x, end='') #side numbers
        print(': ', end = '')
        
        for y in range(screenInfo.size):
            print(screenInfo.matrix[x, y] , end = ' ')
        print('')
    x = 0
    y = 0
    
    
def initSetup():
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(btnRight, GPIO.IN)
    GPIO.setup(btnUp, GPIO.IN)
    GPIO.setup(btnDown, GPIO.IN)
    GPIO.setup(btnLeft, GPIO.IN)
    
    GPIO.add_event_detect(btnRight, GPIO.RISING)
    GPIO.add_event_detect(btnUp, GPIO.RISING)
    GPIO.add_event_detect(btnLeft, GPIO.RISING)
    GPIO.add_event_detect(btnDown, GPIO.RISING)
    
    inputValid = 0
    screenInfo = screen()
    if ~inputValid:
        size = input('What size screen would you like? ')
        try:
            val = int(size)
        except ValueError:
            print('Invalid Entry: Please enter a number')
            
        screenInfo.size = val
        inputValid = 1
    
    for x in range(screenInfo.size): #initialize matrix with empty spaces
        for y in range(screenInfo.size):
            screenInfo.matrix[x, y] = ' ' 
    
    screenInfo.x = math.floor(screenInfo.size/2)
    screenInfo.y = math.floor(screenInfo.size/2)
    screenInfo.matrix[screenInfo.x, screenInfo.y] = 'x' #draw X in center of screen
    
    return screenInfo
            
            
def main():
    screenInfo = initSetup()
    
    while True:
        printScreen(screenInfo)
        userInputReceived = False
        #wait for user input before redrawing screen
        while userInputReceived == False:
            if GPIO.event_detected(btnRight):
                time.sleep(0.1)
                userInputReceived = True
                if screenInfo.x > 0:
                    screenInfo.x -= 1
            if GPIO.event_detected(btnUp):
                time.sleep(0.1)
                userInputReceived = True
                if screenInfo.y > 0:
                    screenInfo.y -= 1
            if GPIO.event_detected(btnLeft):
                time.sleep(0.1)
                userInputReceived = True
                if screenInfo.x < screenInfo.size - 1:
                    screenInfo.x += 1
            if GPIO.event_detected(btnDown):
                time.sleep(0.1)
                userInputReceived = True
                if screenInfo.y < screenInfo.size - 1:
                    screenInfo.y += 1
        screenInfo.matrix[screenInfo.x, screenInfo.y] = 'x' #put x at new position in matrix
    
main()







