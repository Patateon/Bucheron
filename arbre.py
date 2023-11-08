from Enum import enum

class State(enum):
        lowTree = 0
        midTree = 1
        highTree = 2
        fruitTree = 3


class Arbre():

    def __init__(self, x, y):
        self.pos = pos
        self.state = State.lowTree

    def grow(self):
        if (self.state == State.lowTree or self.state == State.midTree):
            self.state += 1

    def growFruits(self):
        if (self.state == State.highTree):
            self.state += 1
    
