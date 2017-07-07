import pygame
import sys
from pygame.locals import *
from time import sleep
import os

white = (255,255,255)
black = (0,0,0)


def window():
    pygame.init()
    pygame.display.set_caption('Body Data')
    screen = pygame.display.set_mode((1080,150), 0, 32)
    screen.fill((white))
    pygame.display.update()
    
    return screen


def addText(screen, value):
    font = pygame.font.Font('Monotxt.ttf', 70)
    screen.blit(font.render('PULSE: ' + str(value), True, (255,0,0)), (0, 50))
    pygame.display.update()

def showValue(sensorValue):
    screen = window()
    addText(screen, sensorValue)
    sleep(3)


