from segments import Segments
import numpy as np
import cmath
from shell import Shell


#def rotate(z, theta):
#    return cmath.rect(abs(z), cmath.phase(z) - theta)


def rotate(z, theta):
    return (cmath.cos(-theta)+cmath.sin(-theta)*1j) * z


class Tank(object):
    def __init__(self, x, y, w=16, h=30, body_angle=0):
        self.coor = x + y * 1j
        self.body = w + h * 1j
        self.body_angle = body_angle

        self.segs = Segments([
            x - h / 2 + 1j * (y - w / 2),
            x + h / 2 + 1j * (y - w / 2),
            x + h / 2 + 1j * (y + w / 2),
            x - h / 2 + 1j * (y + w / 2),
            x - h / 2 + 1j * (y - w / 2)
        ])

        self.turret_theta = 0
        self.turret_end = 20

        self.shell = None

    def move(self, tire_r, tire_l):
        v = (tire_r + tire_l) / 2
        v = rotate(v, self.body_angle)

        omega = (tire_r - tire_l) / 2
        omega *= 0.05

        self.body_angle += omega
        self.coor += v

        for i, v_coor in enumerate(self.segs):
            v_coor += v
            vz = v_coor - self.coor
            vz = rotate(vz, omega)
            self.segs[i] = self.coor + vz

        self.rotate_turret(omega)

    def rotate_turret(self, theta):
        self.turret_end = rotate(self.turret_end, theta)

    def shot(self):
        self.shell = Shell(self.coor.real+self.turret_end.real, self.coor.imag+self.turret_end.imag, 10, cmath.phase(self.turret_end))

    def draw(self, pygame, screen):
        self.segs.draw(pygame, screen)
        pygame.draw.line(screen, [0, 0, 0], (self.coor.real, self.coor.imag),
                         (self.coor.real + self.turret_end.real, self.coor.imag + self.turret_end.imag), 1)
