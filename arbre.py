from enum import Enum
from valueGrid import valueGrid


class Arbre():

    def __init__(self, x, y):
        self.pos = [x, y]
        self.state = State.lowTree

    def grow(self):
        if (self.state == State.lowTree or self.state == State.midTree):
            self.state += 1

    def growFruits(self):
        if (self.state == State.highTree):
            self.state += 1

    def setPos(self, x, y): # Peut etre utile mais normalement non
        self.pos = [x, y]

    def getPos(self):
        return self.pos

    def setState(self, state:State):
        self.state = state

    def getState(self):
        return self.state
    
