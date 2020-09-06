#!/usr/bin/env python3

import pygame, sys, os, time
from pygame.locals import *

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]

cont = True
pressed = 0

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
    print('x is: ', x, '\ny is:', y)

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: 
        if x < xBound:
            x+=50
    # if key[pygame.K_RIGHT] and key[pygame.K_UP]: 
    #     if x < xBound:
    #         x+=50
    #     if y > 0:
    #         y-=50
    # if key[pygame.K_RIGHT] and key[pygame.K_DOWN]: 
    #     if x < xBound:
    #         x+=50
    #     if y < yBound:
    #         y+=50 
    if key[pygame.K_LEFT]: 
        if x > 0:
            x-=50
    # if key[pygame.K_LEFT] and key[pygame.K_UP]: 
    #     if x > 0:
    #         x-=50
    #     if y > 0:
    #         y-=50
    # if key[pygame.K_LEFT] and key[pygame.K_DOWN]: 
    #     if x > 0:
    #         x-=50
    #     if y < yBound:
    #         y+=50
    if key[pygame.K_UP]: 
        if y > 0:
            y-=50
    if key[pygame.K_DOWN]: 
        if y < yBound:
            y+=50
    time.sleep(.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            #clear the screen
            screen.fill(white)
        