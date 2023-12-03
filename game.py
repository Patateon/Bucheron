#!/usr/bin/env python3
import arbre
import agent
from grille import *
from astar import *
import random
import numpy as np

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
        self.generateGoals()

    def generateTree(self):
        nbA = 0
        while nbA!=self.nbArbres:
            newArbre = (random.randint(0,self.grille.y - 1),random.randint(0,self.grille.x - 1))
            typeArbre = random.randint(1,4)
            if(self.grille.getCell(newArbre) == 0):
                self.grille.setCell(newArbre, State(typeArbre))
                thatArbre = arbre.Arbre(newArbre[1], newArbre[0], State(typeArbre))
                self.arbres.append(thatArbre)
                nbA +=1

    def generateAgent(self):
        nbA = 0
        while nbA!=self.nbAgents:
            newAgent = (random.randint(0,self.grille.y - 1),random.randint(0,self.grille.x - 1))
            if(self.grille.getCell(newAgent) == 0):
                self.grille.setCell(newAgent, State.lumber)
                #On trouve l'arbre le plus proche
                arbreGoal = self.getClosestTree(newAgent[1], newAgent[0])
                arbreGoalPos = arbreGoal.getPos()
                #On trouve une position adjacente a l'arbre le plus proche
                posGoal = self.getAdjacentPos(newAgent[1], newAgent[0], arbreGoalPos[0], arbreGoalPos[1])
                thatAgent = agent.Agent(newAgent[1], newAgent[0], arbreGoalPos[0], arbreGoalPos[1], posGoal[0], posGoal[1])
                self.agents.append(thatAgent)
                nbA +=1

    def getClosestTree(self, agentX, agentY):
        closest = 0
        arbrePos = self.arbres[0].getPos()
        dist1 = abs(agentX - arbrePos[0]) + abs(agentY - arbrePos[1])
        for i in range(1, len(self.arbres)):
            arbrePos = self.arbres[i].getPos()
            dist2 = abs(agentX - arbrePos[0]) + abs(agentY - arbrePos[1])
            if(dist2 < dist1):
                dist1 = dist2
                closest = i
        return self.arbres[closest]

    #On veux couper un Arbre donc on trouve une position adjacente à celui-ci qui est la plus proche de l'agent:
    def getAdjacentPos(self, agentX, agentY, arbreX, arbreY):
        distX = abs(agentX - arbreX)
        distY = abs(agentY - arbreY)
        if(distX < distY):
            if(agentY < arbreY):
                return [arbreX, arbreY - 1]
            else:
                return [arbreX, arbreY + 1]
        else:
            if(agentX < arbreX):
                return [arbreX - 1, arbreY]
            else:
                return [arbreX + 1, arbreY]
        return [arbreX + 1, arbreY]




    def generateGoals(self):
        print("generateGoals()")
        for agent in self.agents:
            print("-----------")
            print("agent.pos :", agent.pos)
            print("agent.arbreGoal :", agent.arbreGoal)
            print("agent.posGoal :", agent.posGoal)
            astar = Astar(self.grille)
            astar.startSearch(np.array(agent.pos), np.array(agent.posGoal))
            #astar.showPath()
            agent.setPath(astar.path)
        print("-------------------")

    def update(self):
        for agent in self.agents:
            lastPos = agent.getPos()
            agent.doNextMove(self.grille)
            self.setCell([lastPos[1], lastPos[0]], 0)
            self.setCell([agent.getPos()[1], agent.getPos()[0]], 5)

    def getCell(self, position):
        return self.grille.getCell(position)

    def setCell(self, position, donnee):
        self.grille.setCell(position, donnee)
