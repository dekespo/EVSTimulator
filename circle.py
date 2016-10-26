import constants as CONST
from random import randint  

class Circle:
    def __init__(self, pos = None, radius = 25):
        if pos == None:
            pos = ( randint(0, CONST.window.width), randint(0, CONST.window.height) ) # randomness does not work in parameter
        self.pos = pos
        self.radius = radius
