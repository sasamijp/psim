# coding=utf-8
from itertools import chain
import numpy as np
import util


class Field:
    def __init__(self, bullets, tank_controls, objects, width, height):
        self.bullets = bullets
        self.tank_controls = tank_controls
        self.objects = objects
        self.width = width
        self.height = height
        self.all_lines = list(chain.from_iterable([seg.lines for seg in self.objects]))

    def update(self):
        self.update_bullets()
        self.update_tanks()

        for i, t in enumerate(self.tank_controls):
            start_p, points = t.tank.coor, t.tank.get_sight_line_all()

            for j, p in enumerate(points):
                for l in self.all_lines:
                    cross = util.cross_point(start_p, p, l[0], l[1])
                    if cross is not None:
                        if np.linalg.norm(cross - start_p) < np.linalg.norm(self.tank_controls[i].tank.P[j] - start_p):
                            self.tank_controls[i].tank.P[j] = cross

                for k, tt in enumerate(self.tank_controls):
                    if i == k:
                        continue
                    for tt_l in tt.tank.segs.get_lines():
                        cross = util.cross_point(start_p, p, tt_l[0], tt_l[1])
                        if cross is not None:
                            if np.linalg.norm(cross - start_p) < np.linalg.norm(self.tank_controls[i].tank.P[j] - start_p):
                                self.tank_controls[i].tank.P[j] = cross

    def update_bullets(self):
        deletes = []
        for i, b in enumerate(self.bullets):
            if self.__is_out_of_stage(b):
                deletes.append(i)
                break

            for l in self.all_lines:
                if util.intersection2d(b[0], b[1], l[0], l[1]):
                    deletes.append(i)
                    break
            b.update()

        for d_i in reversed(deletes):  # indexが指す値が変わらないようにするためのreverse
            del self.bullets[d_i]

    def __is_out_of_stage(self, bullet):
        return not (0 < bullet[0][0] < self.width and
                    0 < bullet[0][1] < self.height and
                    0 < bullet[1][0] < self.width and
                    0 < bullet[1][1] < self.height)

    def update_tanks(self):
        r = 30 ** 2
        for t in self.tank_controls:
            t.update()
            if t.tank.bullet is not None:
                self.bullets.append(t.tank.bullet)
                t.tank.bullet = None

            for l in self.all_lines:
                if util.min_distance2d2(l[0], l[1], t.tank.coor) < r:
                    # 速度ベクトルの逆方向に移動させて移動を0にする
                    t.tank.update_coor(t.tank.coor_t1 - t.tank.coor, 0)

        deletes = []
        for i, t in enumerate(self.tank_controls):
            for b in self.bullets:
                if self.is_hit(t.tank, b):
                    deletes.append(i)
                    break

        for d_i in reversed(deletes):
            del self.tank_controls[d_i]

    def is_hit(self, tank, bullet):
        for l in tank.segs.get_lines():

            if util.intersection2d(l[0], l[1], bullet[0], bullet[1]):
                return True
        return False

    def draw(self, pygame, screen):
        for o in self.objects:
            o.draw(pygame, screen)

        for t in self.tank_controls:
            t.tank.draw(pygame, screen)

        for b in self.bullets:
            b.draw(pygame, screen)
