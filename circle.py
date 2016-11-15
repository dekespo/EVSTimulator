from random import randint  

class Circle:
    def __init__(self, frameSizes, pos = None, radius = 25):
        if pos == None:
            pos = ( randint(0, frameSizes[0]), randint(0, frameSizes[1]) ) # randomness does not work in parameter
        self.pos = pos
        self.radius = radius

    def __repr__(self):
        x, y = self.pos
        r = self.radius
        return "(x, y, r) = " + str(x) + " " + str(y) + " " + str(r)
