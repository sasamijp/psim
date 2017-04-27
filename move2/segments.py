
class Segments(list):
    def __init__(self, vectors):
        super(Segments, self).__init__()
        self.add_segments(vectors)

    def add_segments(self, vectors):
        self.extend(vectors)

    def draw(self, pygame, screen):
        for i in range(len(self)-1):
            pygame.draw.line(screen, [0, 0, 0], (self[i][0], self[i][1]), (self[i+1][0], self[i+1][1]), 1)
