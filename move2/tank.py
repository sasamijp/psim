import util
import numpy as np
import segments as seg
import bullet


class Tank:
    def __init__(self, x, y, w, h, body_angle):
        self.coor = np.array([x, y])
        self.coor_t1 = np.array([x, y])
        self.body = np.array([w, h])
        self.body_angle = body_angle

        self.segs = seg.Segments([
            [x - h / 2, (y - w / 2)],
            [x + h / 2, (y - w / 2)],
            [x + h / 2, (y + w / 2)],
            [x - h / 2, (y + w / 2)],
        ])

        self.turret_theta = 0
        self.turret_end = 20

        self.tire_r = 0
        self.tire_l = 0

        self.tire_fric = 1.1

        self.bullet = None

        self.view_angle_size = np.pi / 1.5
        self.view_angle_theta = 0

    def update(self, d_tire_r, d_tire_l):
        self.tire_r = d_tire_r
        self.tire_l = d_tire_l

        omega = (self.tire_r - self.tire_l) / 2
        omega *= 0.05
        self.rotate_turret(omega)

        v = (self.tire_r + self.tire_l) / 2 * np.array([np.cos(self.body_angle),
                                                        np.sin(self.body_angle)])

        self.coor_t1 = np.copy(self.coor)
        self.update_coor(v, omega)

    def update_coor(self, v, omega):
        self.coor += v
        self.body_angle += omega

        for i, v_coor in enumerate(self.segs):
            v_coor += v
            vz = v_coor - self.coor
            vz = util.rotate(vz, omega)
            self.segs[i] = self.coor + vz

    def rotate_turret(self, theta):
        self.turret_theta += theta

    def rotate_view(self, theta):
        self.view_angle_theta += theta

    def shot(self):
        self.bullet = bullet.Bullet(self.coor[0] + self.turret_end * np.cos(self.turret_theta),
                                    self.coor[1] + self.turret_end * np.sin(self.turret_theta),
                                    50 * np.cos(self.turret_theta),
                                    50 * np.sin(self.turret_theta))

    def get_state_all(self):
        return np.array([
            self.body_angle,
            self.tire_r,
            self.tire_fric,
            self.coor[0],
            self.coor[1],
            self.turret_theta

        ])

    def draw(self, pygame, screen):
        self.segs.draw(pygame, screen)
        pygame.draw.line(screen, [0, 0, 0], (self.coor[0], self.coor[1]),
                         (self.coor[0] + self.turret_end * np.cos(self.turret_theta),
                          self.coor[1] + self.turret_end * np.sin(self.turret_theta)), 1)

        l = 100
        x = self.coor[0]
        y = self.coor[1]

        # pygame.draw.line(screen, [255, 0, 0],
        #                  (x, y),
        #                  (
        #                      x + l * np.cos(-self.view_angle_size / 2.0 + self.view_angle_theta),
        #                      y + l * np.sin(-self.view_angle_size / 2.0 + self.view_angle_theta)
        #                  )
        #                  , 1)
        #
        # pygame.draw.line(screen, [255, 0, 0],
        #                  (x, y),
        #                  (
        #                      x + l * np.cos(self.view_angle_size / 2.0 + self.view_angle_theta),
        #                      y + l * np.sin(self.view_angle_size / 2.0 + self.view_angle_theta)
        #                  )
        #                  , 1)
