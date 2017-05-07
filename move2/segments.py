import numpy as np


class Segments(list):
    def __init__(self, vectors, closed=True, block=True):
        super(Segments, self).__init__()
        self.closed = closed
        self.block = block
        self.__add_segments([np.array(v) for v in vectors])

        self.lines = []
        self.generate_lines()

    def __add_segments(self, vectors):
        self.extend(vectors)

    def generate_lines(self):
        for i in range(len(self) - 1):
            self.lines.append((np.array(self[i]), np.array(self[i+1])))

        if self.closed:
            self.lines.append((np.array(self[-1]), np.array(self[0])))

    def get_lines(self):
        self.lines = []
        self.generate_lines()
        return self.lines

    def draw(self, pygame, screen):
        pygame.draw.lines(screen, (0, 0, 0), self.closed, self, 1)
