from state import *

class Arbre():

    def __init__(self, x, y, state:State):
        self.pos = [x, y]
        self.state = state
        self.taken = False
        self.pv = 5

    def grow(self):
        if (self.state == State.lowTree or self.state == State.midTree):
            self.state += 1

    def growFruits(self):
        if (self.state == State.highTree):
            self.state += 1

    def getPos(self):
        return [self.pos[1], self.pos[0]]

    def setPos(self, x, y): # Peut etre utile mais normalement non
        self.pos = [x, y]

    def getState(self):
        return self.state

    def setState(self, state:State):
        self.state = state
    
    def getPV(self):
        return self.pv

    def setPV(self, pv):
        self.pv = pv

    def getTaken(self):
        return self.taken

    def setTaken(self, taken):
        self.taken = taken