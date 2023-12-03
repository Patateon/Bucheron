import numpy as np
from heapq import *

from node import *
from game import *


class Astar():

    def __init__(self, grille):
        self.grille = grille
        self.openSet = []
        self.closeSet = {None}
        self.path = []
        self.pathFound = False

    def dist(self, n1, n2):
        return np.linalg.norm(n1.getPosition() - n2.getPosition())

    def distManhattan(self, n1, n2):
        return np.linalg.norm(n1.getPosition() - n2.getPosition(), ord=1)

    def startSearch(self, start, end):
        self.clearSet()
        start = Node(start, True)
        end = Node(end, True)
        start.setg_cost(0)
        start.seth_cost(self.dist(start, end))
        # self.openSet = heapify(self.openSet)
        # print(self.openSet)
        self.path = self.findPath(start, end)

    """ 
    Pourrait servir qui sait
    def minF_set(self):
        minNode = self.openSet[0]
        for node in self.openSet:
            minNode = node if (node.f_cost()<=minNode.f_cost() and node.geth_cost()<minNode.geth_cost()) else minNode
        return minNode
    """

    def getFrontier(self, n):
        position = n.getPosition()
        x, y = position[0], position[1]
        neighbours = []
        for offset in np.array([[1, 0], [0, 1], [-1, 0], [0, -1]]):
            tmp = offset + position
            if (tmp[0] >= 0 and tmp[0] < self.grille.x and tmp[1] >= 0 and tmp[1] < self.grille.y):
                if (self.grille.getCell([tmp[1], tmp[0]]) == State.vide):
                    neighbours.append(Node(tmp, True))
                else:
                    neighbours.append(Node(tmp, False))
        return neighbours

    def clearSet(self):
        self.pathFound = False
        self.openSet = []
        self.closeSet = {None}

    def backTrack(self, end, start):
        path = []
        currentNode = end
        while (currentNode != start):
            path.append(currentNode)
            currentNode = currentNode.parent
        path.append(start)
        return path[::-1] 

    def findPath(self, start, end):
        heappush(self.openSet, start)

        while len(self.openSet):
            if len(self.openSet) == 1:
                current = self.openSet[0]
                self.openSet = []
            else:
                current = heappop(self.openSet)
            self.closeSet.add(current)

            if (current == end):
                self.pathFound = True
                return self.backTrack(current, start)

            for neighbour in self.getFrontier(current):
                if (not neighbour.walkable or neighbour in self.closeSet):
                    continue

                g_cost = current.getg_cost() + 1

                if (neighbour.getg_cost() == None):
                    neighbour.setg_cost(g_cost + 1)

                if (g_cost < neighbour.getg_cost() or not neighbour in self.openSet):
                    neighbour.setg_cost(g_cost)
                    neighbour.seth_cost(self.distManhattan(neighbour, end))
                    neighbour.setParent(current)
                    if (not neighbour in self.openSet):
                        heappush(self.openSet, neighbour)
        
        return False

    def showPath(self):
        if (self.path == False):
            print("No path found !\n")
        else:
            for node in self.path:
                if (self.grille.getCell([node.getPosition()[1], node.getPosition()[0]]) == State.vide):
                    self.grille.setCell([node.getPosition()[1], node.getPosition()[0]], 6)
