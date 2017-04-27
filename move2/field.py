class Field:
    def __init__(self):
        self.bullets = []
        self.tank_controlls = []

    def update(self):
        for t in self.tank_controlls:
            t.update()

        for b in self.bullets:
            b.update()

    def draw(self, pygame, screen):
        for t in self.tank_controlls:
            t.tank.draw(pygame, screen)

        for b in self.bullets:
            b.draw(pygame, screen)
