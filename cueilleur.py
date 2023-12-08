#!/usr/bin/env python3
from state import *

NORD = tuple([0, -1])
SUD = tuple([0, 1])
EST = tuple([1, 0])
OUEST = tuple([-1, 0])

class Cueilleur:
    def __init__(self, cueillX, cueillY):
        self.pos = [cueillX, cueillY]
        self.goal = 0
        self.arbreGoal = []
        self.posGoal = []
        self.path = []

    def getPos(self):
        return self.pos

    def setPos(self, x, y): # Peut etre utile mais normalement non
        self.pos = [x, y]

    def getGoal(self):
        return self.goal

    def setGoal(self, x):
        self.goal = x

    def getArbreGoal(self):
        return self.arbreGoal

    def setArbreGoal(self, x, y):
        self.arbreGoal = [x, y]

    def getPosGoal(self):
        return self.posGoal

    def setPosGoal(self, x, y):
        self.posGoal = [x, y]

    def getPath (self):
        return self.path

    def setPath(self, path):
        self.path = path
        #On enlève la première position du path, qui est la pos du bucheron
        print("setpath")
        self.path.pop(0)

    def can_move(self, x, y, grille):
        print("next move :")
        print(grille.grille[y][x])
        if(grille.grille[y][x] == State.vide):
            return True
        return False

    def doNextMove(self, grille):
        #si but atteint
        print(self.getPos())
        print(self.getPosGoal())
        if(self.getPos() == self.getPosGoal()):
            print("Goal atteint")
            return
        #si path vide
        elif(len(self.path) == 0):
            print("pas de path")
            return
        #Cas où on doit faire un move
        nextMove = self.path[0].getPosition()
        if(self.can_move(nextMove[0], nextMove[1], grille)):
            self.setPos(nextMove[0], nextMove[1])
            self.path.pop(0)
        #cas bloqué
        else:
            print("cannot move")
