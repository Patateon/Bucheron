#!/usr/bin/env python3
import arbre
from grille import *
import random

class Game:
    def __init__(self, dimX, dimY, nbAgents, nbArbres):
        self.grille = Grille(dimX, dimY)
        self.nbAgents = nbAgents
        self.nbArbres = nbArbres
        self.arbres = []
        self.agents = []
        self.initGame()

    def initGame(self):
        self.generateTree()
        self.generateAgent()

    def generateTree(self):
        nbA = 0
        while nbA!=self.nbArbres:
            newArbre = (random.randint(0,self.grille.y - 1),random.randint(0,self.grille.x - 1))
            typeArbre = random.randint(1,4)
            if(self.grille.getCell(newArbre) == 0):
                self.grille.setCell(newArbre, State(typeArbre))
                thatArbre = arbre.Arbre(newArbre[0], newArbre[1], State(typeArbre))
                self.arbres.append(thatArbre)
                nbA +=1

    def generateAgent(self):
        nbA = 0
        while nbA!=self.nbAgents:
            newAgent = (random.randint(0,self.grille.y - 1),random.randint(0,self.grille.x - 1))
            if(self.grille.getCell(newAgent) == 0):
                self.grille.setCell(newAgent, State.lumber)
                self.agents.append(newAgent)
                nbA +=1