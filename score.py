
class Score():

    def __init__(self):
        self.score = 0
        self.nbScoreBois = 0
        self.nbFruit = 0

    def updateScore(self):
        self.score = nbScoreBois + nbFruit

    def getScore(self):
        return self.score

    def setNbScoreBois(self, nbScoreBois):
        self.nbScoreBois = nbScoreBois

    def getNbScoreBois(self):
        return self.nbScoreBois

    def setNbFruit(self, nbFruit):
        self.nbFruit = nbFruit

    def getNbFruit(self):
        return self.nbFruit