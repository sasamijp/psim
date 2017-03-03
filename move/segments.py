
class Segments(list):
    def __init__(self, vectors):
        super(Segments, self).__init__()
        self.add_segments(vectors)

    def add_segments(self, vectors):
        self.extend(vectors)

    def draw(self, pygame, screen):
        for i in range(len(self)-1):
            pygame.draw.line(screen, [0, 0, 0], (self[i].real, self[i].imag), (self[i+1].real, self[i+1].imag), 1)
