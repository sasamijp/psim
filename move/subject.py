# -*- coding:utf-8 -*-

from observer import Observer
import random


# データ入力・加工
class Subject:
    def __init__(self):
        self.observer = Observer()

    def execute(self, data):

        if random.random() < 0.05:
            data.tanks[0].shot()

        for tank in data.tanks:

            if tank.shell is not None:
                data.shells.append(tank.shell)
                tank.shell = None

            tank.move(0.7, 5)
            tank.rotate_turret(0.1)

        self.observer.update(data)
