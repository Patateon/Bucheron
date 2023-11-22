#!/usr/bin/env python3
from enum import Enum
import Arbre

class Game:
    def __init__(self, dimX, dimY, nbAgent, nbbArbres):
        self.grille = Grille(dimX, dimY)
        self.nbAgents = nbAgents
        self.nbArbres = nbArbres
        self.arbres = []

        geretardeGrid(dimX, dimY)

    def generateTree(self, nombreArbre: int):
        nbA = 0
        while nbA!=nbArbres:
            newArbre = (randint(0,self.y),randint(0,self.x))
            typeArbre = randint(2,3)
            if(grille.getCell(newArbre) == 0):
                grille.setCell(newArbre, 1)
                arbres.append(newArbre)
                nbA +=1
