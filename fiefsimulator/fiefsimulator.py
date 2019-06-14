import random as rand

def dieRoller(nrOfDice, sides, OB = False):
    actualNrOfDice = nrOfDice
    sum = 0
    rolls = []
    rollNr = 0
    while rollNr < actualNrOfDice:
        roll = rand.randint(1,sides)
        if OB == True and sides == 6 and roll == 6:
            actualNrOfDice = actualNrOfDice+2
        else:
            sum = sum+roll
            rolls.append(roll)
        rollNr = rollNr+1
    return sum, rolls

class Fiefdom:

    def __init__(self):
        self.industries = {}
        self.industries["Farming"] = 1
        self.industries["Livestock"] = 1
        self.industries["Forest"] = 1
        self.industries["Fishing"] = 0
        self.industries["Hunting"] = 1
        self.rank = 1 #noble rank 1 = Landed Knight 5 = King/similar
        self.qualityPoints = 25
        self.forestArea = 0 #Acres

    def changeIndustryQuality(self, industry, newValue):
        cost = 0
        currValue = self.industries[industry]
        if newValue > self.industries[industry]:
            for x in range(newValue,currValue,-1):
                cost = cost+x
        else:
            for x in range(currValue,newValue):
                cost = cost+x
            cost = cost*-1

        if cost > self.qualityPoints:
            return "You do not have enough points", self.qualityPoints, cost
        else:
            self.qualityPoints = self.qualityPoints-cost
            self.industries[industry] = newValue
            return self.qualityPoints, cost

    def printIndustryQualities(self):
        for k,v in oakheart.industries.iteritems():
            print "%s:%d" % (k,v)
    def calculateForestArea(self):
        self.forestArea = self.industries["Forest"]*dieRoller(3,6,True)[0]*10
        return self.forestArea


oakheart = Fiefdom()

print oakheart.changeIndustryQuality("Forest", 3)
print oakheart.calculateForestArea()
