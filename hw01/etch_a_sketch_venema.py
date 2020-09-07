#!/usr/bin/env python3

import pygame, sys, os, time
from pygame.locals import *

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]

cont = True
rightPressed = 0
leftPressed = 0
upPressed = 0
downPressed = 0

while cont:
    screenSize = input("What size screen would you like? Small, Medium, or Large?")
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
    print('Invalid input, please try again \n')

xBound = 100*screenSize
yBound = 100*screenSize

screen = pygame.display.set_mode((xBound, yBound))


#Set initial placement of cursor and color of screen
x = int(xBound/2)
y = int(yBound/2)
screen.fill(white)

while True:
    pygame.draw.circle(screen, black, (x,y), 2)
    pygame.display.update()
    #print('x is: ', x, '\ny is:', y)

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: 
        if (x < xBound) & ~rightPressed:
            x+=50
        rightPressed = 1
        #time.sleep(0.5)
    if key[pygame.K_LEFT] & ~leftPressed: 
        if x > 0:
            x-=50
        leftPressed = 1
    if key[pygame.K_UP] & ~upPressed: 
        if y > 0:
            y-=50
        upPressed = 1
    if key[pygame.K_DOWN] & ~downPressed: 
        if y < yBound:
            y+=50
        downPressed = 1
    if key[pygame.K_RIGHT] == False:
        rightPressed = 0
    if key[pygame.K_LEFT] == False:
        leftPressed = 0
    if key[pygame.K_UP] == False:
        upPressed = 0
    if key[pygame.K_DOWN] == False:
        downPressed = 0
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            #clear the screen
            screen.fill(white)
        