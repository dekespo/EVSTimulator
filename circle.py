import constants as CONST
from random import randint  

class Circle:
    def __init__(self, pos = None, radius = 25):
        if pos == None:
            pos = ( randint(0, CONST.simulationWindow.width), randint(0, CONST.simulationWindow.height) ) # randomness does not work in parameter
        self.pos = pos
        self.radius = radius

    def __repr__(self):
        x, y = self.pos
        r = self.radius
        return "(x, y, r) = " + str(x) + " " + str(y) + " " + str(r)
