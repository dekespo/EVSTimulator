from random import randint


class Circle:
    def __init__(self, frameSizes, pos=None, radius=25):
        if pos is None:
            # Randomness does not work in parameter
            pos = (randint(0, frameSizes[0]), randint(0, frameSizes[1]))
        self.pos = pos
        self.radius = radius

    def __repr__(self):
        x, y = self.pos
        r = self.radius
        return "(x, y, r) = " + str(x) + " " + str(y) + " " + str(r)
