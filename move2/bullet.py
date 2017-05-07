import numpy as np
import segments


class Bullet(segments.Segments):
    def __init__(self, x, y, dx, dy):
        super(Bullet, self).__init__([(x, y), (x + dx, y + dy)], closed=False, block=True)

        self.v = np.array([dx, dy])

    def update(self):
        self[0][0] = self[1][0]
        self[0][1] = self[1][1]
        self[1] += self.v
