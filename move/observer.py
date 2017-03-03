# -*- coding:utf-8 -*-


# データの描画
class Observer:
    def __init__(self):
        pass

    def update(self, data):
        for tank in data.tanks:
            tank.draw(data.pygame, data.screen)

        data.wall.draw(data.pygame, data.screen)

        for shell in data.shells:
            shell.draw(data.pygame, data.screen)
