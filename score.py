
class Score():

    def __init__(self, valueBois, valueFruit):
        self.score = 0
        self.nbBois = 0
        self.nbFruit = 0
        self.valueBois = valueBois
        self.valueFruit = valueFruit

    def updateScore(self):
        self.score = self.nbBois + self.nbFruit

    def increaseWoodScore(self, number):
        self.nbBois += self.valueBois * number

    def increaseFruitScore(self):
        self.nbFruit += self.valueFruit

    def plantFruit(self):
        self.nbFruit -= self.valueFruit

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

    def getValueFruit(self):
        return self.valueFruit