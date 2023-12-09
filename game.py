#!/usr/bin/env python3
import arbre
import agent
from score import *
import cueilleur
from grille import *
from astar import *
import random
import numpy as np

class Game:

    def __init__(self, dimX, dimY, nbAgents, nbCueilleurs, nbArbres, valueBois, valueFruit):
        self.grille = Grille(dimX, dimY)
        self.nbAgents = nbAgents
        self.nbArbres = nbArbres
        self.nbCueilleurs = nbCueilleurs
        self.arbres = []
        self.agents = []
        self.cueilleurs = []
        self.treshold = 5
        self.score = Score(valueBois, valueFruit)
        self.initGame()


    def initGame(self):
        self.generateTree()
        self.generateAgent()
        self.generateCueilleur()
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
                thatAgent = agent.Agent(newAgent[1], newAgent[0])
                self.agents.append(thatAgent)
                nbA +=1

    def generateCueilleur(self):
        nbA = 0
        while nbA!=self.nbCueilleurs:
            newCueilleur = (random.randint(0,self.grille.y - 1),random.randint(0,self.grille.x - 1))
            if(self.grille.getCell(newCueilleur) == 0):
                self.grille.setCell(newCueilleur, State.harvest)
                #On trouve l'arbre le plus proche
                thatCueilleur = cueilleur.Cueilleur(newCueilleur[1], newCueilleur[0])
                self.cueilleurs.append(thatCueilleur)
                nbA +=1


    def getClosestTree(self, agentX, agentY):
        closest = 0
        arbrePos = self.arbres[0].getPos()
        dist1 = abs(agentX - arbrePos[0]) + abs(agentY - arbrePos[1])
        for i in range(1, len(self.arbres)):
            arbrePos = self.arbres[i].getPos()
            if(not self.arbres[i].getTaken()):
                dist2 = abs(agentX - arbrePos[0]) + abs(agentY - arbrePos[1])
                if(dist2 < dist1):
                    dist1 = dist2
                    closest = i
        self.arbres[closest].setTaken(True)
        return self.arbres[closest]

    def getClosestFruitTree(self, agentX, agentY):
        closest = 0
        dist1 = 999999999 # aled ce truc
        for i in range(len(self.arbres)):
            if(self.arbres[i].getState() == State.fruitTree):
                # print("FRUIIIIIT")
                arbrePos = self.arbres[i].getPos()
                if(not self.arbres[i].getTaken()):
                    dist2 = abs(agentX - arbrePos[0]) + abs(agentY - arbrePos[1])
                    if(dist2 < dist1):
                        dist1 = dist2
                        closest = i
        self.arbres[closest].setTaken(True)
        if(self.arbres[closest].getState() == State.fruitTree):
            # print("A")
            return self.arbres[closest]
        else:
            print("B")
            return None

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


    def growArbres(self):
        # nbArbreToGrow = random.randint(0, self.nbArbres-1)
        for index_arbre in range(self.nbArbres):
            if (random.randint(0, 1)):
                self.arbres[index_arbre].grow()

    def growFruits(self):
        # nbArbreToGrow = random.randint(0, self.nbArbres-1)
        for index_arbre in range(self.nbArbres):
            if (random.randint(0, 1)):
                self.arbres[index_arbre].growFruits()

    def updateArbre(self):
        for arbre in self.arbres:
            if (arbre.getPV() == 0):
                self.grille.setCell(arbre.getPos(), State.vide)
                self.arbres.remove(arbre)
                self.score.increaseWoodScore()
            self.grille.setCell(arbre.getPos(), arbre.getState())
        for agent in self.agents:
            print(agent.getPosGoal())

    def generateGoalAgent(self, agent):
        # print("generateGoals()")
        # print("-----------")
        #On trouve l'arbre le plus proche
        arbreGoal = self.getClosestTree(agent.getPos()[1], agent.getPos()[0])
        agent.arbreGoal = arbreGoal
        #On trouve une position adjacente a l'arbre le plus proche
        agent.posGoal = self.getAdjacentPos(agent.getPos()[1], agent.getPos()[0], agent.arbreGoal.getPos()[1], agent.arbreGoal.getPos()[0])
        # print("agent.pos :", agent.pos)
        # print("agent.arbreGoal :", agent.arbreGoal)
        # print("agent.posGoal :", agent.posGoal)
        astar = Astar(self.grille)
        astar.startSearch(np.array(agent.pos), np.array(agent.posGoal))
        #astar.showPath()
        if (not astar.getPath()):
            return
        agent.setPath(astar.path)
        agent.setGoal(1)
        #print(agent.path[0].getPosition())
        # print("-------------------")

    def generateGoalCueilleur(self, cueilleur):
        print("-----------")
        arbreGoal = self.getClosestFruitTree(cueilleur.getPos()[1], cueilleur.getPos()[0])
        if (arbreGoal == None):
            cueilleur.setGoal(0)
            return
        cueilleur.arbreGoal = arbreGoal
        #On trouve une position adjacente a l'arbre le plus proche
        cueilleur.posGoal = self.getAdjacentPos(cueilleur.getPos()[1], cueilleur.getPos()[0], cueilleur.arbreGoal.getPos()[1], cueilleur.arbreGoal.getPos()[0])
        print("cueilleur.pos :", cueilleur.pos)
        print("cueilleur.arbreGoal :", cueilleur.arbreGoal.getPos())
        print("cueilleur.posGoal :", cueilleur.posGoal)
        print(cueilleur.arbreGoal.getPos())
        # if(len(cueilleur.arbreGoal)):
        astar = Astar(self.grille)
        astar.startSearch(np.array(cueilleur.pos), np.array(cueilleur.posGoal))
        #astar.showPath()
        if (not astar.getPath()):
            return
        cueilleur.setPath(astar.path)
        cueilleur.setGoal(1)
        # else:
        #     cueilleur.setGoal(0)
        print("-------------------")

    def generateGoals(self):
        for agent in self.agents:
            if(not agent.getGoal()):
                self.generateGoalAgent(agent)
        for cueilleur in self.cueilleurs:
            if(not cueilleur.getGoal()):
                self.generateGoalCueilleur(cueilleur)

    def update(self):
        for agent in self.agents:
            if(agent.getGoal()):
                lastPos = agent.getPos()
                agent.doNextMove(self.grille)
                self.setCell([lastPos[1], lastPos[0]], 0)
                self.setCell([agent.getPos()[1], agent.getPos()[0]], 5)
            else:
                self.generateGoalAgent(agent)
        for cueilleur in self.cueilleurs:
            if(cueilleur.getGoal()):
                lastPos = cueilleur.getPos()
                cueilleur.doNextMove(self.grille)
                self.setCell([lastPos[1], lastPos[0]], 0)
                self.setCell([cueilleur.getPos()[1], cueilleur.getPos()[0]], 6)
            else:
                self.generateGoalCueilleur(cueilleur)

    def getCell(self, position):
        return self.grille.getCell(position)

    def setCell(self, position, donnee):
        self.grille.setCell(position, donnee)
