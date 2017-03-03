from segments import Segments
from tank import Tank


class Data:
    def __init__(self, width, height, pygame, screen):
        self.wall = Segments([])
        self.wall.add_segments([
            10 + 1j * 10,
            width - 10 + 1j * 10,
            width - 10 + 1j * (height - 10),
            10 + 1j * (height - 10),
            10 + 1j * 10
        ])

        self.pygame = pygame
        self.screen = screen

        self.tanks = [Tank(130, 130),
                      ]#Tank(230, 30)]

        self.shells = []
