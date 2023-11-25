import numpy as np

class Node():

    def __init__(self, position, walkable):
        self.position = position
        self.parent = None
        self.g_cost = None
        self.h_cost = None
        self.walkable = walkable

    def f_cost(self):
        return self.g_cost + self.h_cost

    def getPosition(self)->np.ndarray:
        return self.position

    def getg_cost(self):
        return self.g_cost

    def geth_cost(self):
        return self.h_cost

    def setParent(self, parent):
        self.parent = parent

    def setg_cost(self, g):
        self.g_cost = g

    def seth_cost(self, h):
        self.h_cost = h

    def __eq__(self, other):
        return np.array_equal(self.position, other.position)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.f_cost() < other.f_cost()

    def __hash__(self):
        return hash((self.position[0], self.position[1]))