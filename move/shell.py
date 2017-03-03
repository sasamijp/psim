import numpy as np
import cmath


class Shell:
    def __init__(self, x, y, v0, theta):
        self.coor = np.array([x, y], dtype='float64')
        z = cmath.rect(v0, theta)
        self.velocity = np.array([z.real, z.imag])

    def draw(self, pygame, screen):
        pygame.draw.line(screen, [0, 0, 0], self.coor, self.coor + self.velocity, 1)
        self.coor += self.velocity
