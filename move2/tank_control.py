import random


class TankControl:
    def __init__(self, tank):
        self.tank = tank

    def update(self):
        state = self.tank.get_state_all()
        self.tank.update(random.choice(state)/100.0, random.choice(state)/100.0)
        self.tank.rotate_turret(random.choice(state)/10000.0)
        self.tank.shot()
