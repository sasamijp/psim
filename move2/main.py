# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import tank
import field
import tank_control
import bullet
import segments

width = 1000
height = 1000

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test")

field = field.Field(
    [],  # bullets
    [  # tanks
        tank_control.TankControl(tank.Tank(500.0, 900.0, 10.0, 20.0, 0)),
        tank_control.TankControl(tank.Tank(500.0, 200.0, 10.0, 20.0, 0)),
        tank_control.TankControl(tank.Tank(90.0, 500.0, 10.0, 20.0, 0)),
        tank_control.TankControl(tank.Tank(850.0, 500.0, 10.0, 20.0, 0))
    ],
    [  # objects
        segments.Segments([(300, 450), (800, 450), (800, 700), (300, 700)]),
        segments.Segments([(50, 50), (width-50, 50), (width-50, height-50), (50, height-50)])
    ],
    width,
    height
)

while True:
    screen.fill((255, 255, 255))

    field.update()
    field.draw(pygame, screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
