import random


class TankControl:
    def __init__(self, tank):
        self.tank = tank

    def update(self):
        state = self.tank.get_state()
        self.tank.update(random.choice(state), 1)
