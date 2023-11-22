#!/usr/bin/env python3
class Grille:
    def __init__(self, dimX: int, dimY:int):
        self.x=dimX
        self.y=dimY
        self.grille=[[0 for x in self.x] for y in self.y]
    def getCell(self, position):
        return self.grille[position[0]][position[1]]
    def setCell(self, position, donnee):
        self.grille[position[0]][position[1]]=donnee