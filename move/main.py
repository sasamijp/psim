# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
from data import Data
from subject import Subject

width = 1000
height = 500


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test")


data = Data(width, height, pygame, screen)
subject = Subject()

while True:
    screen.fill((255, 255, 255))

    subject.execute(data)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
