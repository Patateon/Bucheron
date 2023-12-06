
class Score():

    def __init__(self, valueBois, valueFruit):
        self.score = 0
        self.nbBois = 0
        self.nbFruit = 0
        self.valueBois = valueBois
        self.valueFruit = valueFruit

    def updateScore(self):
        self.score = nbBois + nbFruit

    def increaseWoodScore(self):
        self.nbBois += valueBois

    def increaseFruitScore(self):
        self.nbFruit += valueFruit

    def getScore(self):
        return self.score

    def setNbBois(self, nbBois):
        self.nbBois = nbBois

    def getNbBois(self):
        return self.nbBois

    def setNbFruit(self, nbFruit):
        self.nbFruit = nbFruit

    def getNbFruit(self):
        return self.nbFruit