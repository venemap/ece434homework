#!/usr/bin/env python3

#setup and imports
import pygame, sys, os
from pygame.locals import *
pygame.init()

#initial constants
white = [255, 255, 255]
black = [0, 0, 0]
cont = True
rightPressed = 0
leftPressed = 0
upPressed = 0
downPressed = 0


def clearScreen(): #clear screen and draw guidelines 100px apart
    screen.fill(white)
    z = 0
    for z in range(screenSize):
        pygame.draw.lines(screen, (211, 211, 211), True, [(z * 100, 0), (z * 100, yBound)])
        pygame.draw.lines(screen, (211, 211, 211), True, [(0, z * 100), (xBound, z * 100)])



while cont: #take in user input and parse
    screenSize = input("What size screen would you like? Small, Medium, or Large?\n")
    screenSize = screenSize.lower()
    if screenSize == 'small':
        screenSize = 4
        cont = False
    elif screenSize == 'medium':
        screenSize = 6
        cont = False
    elif screenSize == 'large':
        screenSize = 8
        cont = False
    else:
         print('Invalid input, please try again \n') #invalid input, restart prompt

#draw screen
xBound = 100*screenSize
yBound = 100*screenSize
screen = pygame.display.set_mode((xBound, yBound))


#Set initial placement of cursor and color of screen
x = int(xBound/2)
y = int(yBound/2)
clearScreen()

while True: #main loop
    #draw and update main circle
    pygame.draw.circle(screen, black, (x,y), 2)
    pygame.display.update()

    key = pygame.key.get_pressed() #array of states for all KB buttons
    #check for key being pressed
    if key[pygame.K_RIGHT]: 
        if (x < xBound) & ~rightPressed:
            x += 50
        rightPressed = 1
    if key[pygame.K_LEFT] & ~leftPressed: 
        if x > 0:
            x -= 50
        leftPressed = 1
    if key[pygame.K_UP] & ~upPressed: 
        if y > 0:
            y -= 50
        upPressed = 1
    if key[pygame.K_DOWN] & ~downPressed: 
        if y < yBound:
            y += 50
        downPressed = 1 
    #check for key being released
    if key[pygame.K_RIGHT] == False:
        rightPressed = 0
    if key[pygame.K_LEFT] == False:
        leftPressed = 0
    if key[pygame.K_UP] == False:
        upPressed = 0
    if key[pygame.K_DOWN] == False:
        downPressed = 0
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Alt+f4 and red x suport
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE: #escape also quits the game
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE: #pressing space clears the board
            clearScreen()


        