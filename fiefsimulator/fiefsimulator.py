import random as rand

availableIndustries = ["Farming", "Fishing", "Forest", "Livestock"]
ordinalNumbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

def printChoices(industries):
    counter = 1
    for indu in availableIndustries:
        print "%d) Change value of %s" % (counter,indu)
        counter = counter+1
    print "%d) Finish changing industry qualities" % counter

def handleInput(choice, fief):
        if int(choice) >0 and int(choice) <= len(availableIndustries):
            print "Which new value would you like for %s?" %availableIndustries[int(choice)-1]
            newValue = raw_input()
            while newValue.isdigit() == False or int(newValue) < 0:
                print "Please enter a numeric value greater than 0."
                newValue = raw_input()
            oakheart.changeIndustryQuality(availableIndustries[int(choice)-1],int(newValue))
            return True
        elif int(choice) == len(availableIndustries)+1:
            return False
        else:
            "Please enter only one of the available digits: 1-%d" %len(availableIndustries)+1
            return True




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
    return sum


class FiefdomFactory:

    def calculateForestArea(self, forestQuality):
        self.forestArea = forestQuality*dieRoller(3,6,True)[0]*10
        return self.forestArea
    def calcNrOfEstates(self, rank):
        if rank == 1:
            return 1
        else:
            tempEstates = dieRoller(rank-1,6,False)-rank
            return max(tempEstates,1)
    def calcNrOfVillages(self):
        return max(dieRoller(1,6,True)-2, 1)
    def calculateVillagePopulation(self):
            return dieRoller(2,6,True)*5

    def calculateVillageLand(self,population):
        return population*dieRoller(3,6,True)
    def calculateEstateLand(self):
        return dieRoller(3,6,True)

    def buildEstates(self, rank):
        estates = []
        nrOfestates = self.calcNrOfEstates(rank)
        print "You have %d estates in yoru fiefdom." %nrOfestates
        for i in range(nrOfestates):
            print "What would you like to name your %s estate" %ordinalNumbers[i]
            name = raw_input()
            estLand = self.calculateEstateLand()
            self.buildVillages(self.calcNrOfVillages(), name)

    def buildVillages(self,nrOfVillages, estateName):
        villages = []
        print "%s has %d villages." %(estateName, nrOfVillages)
        for x in range(nrOfVillages):
            print "What would you like to name the %s village of %s?" %(ordinalNumbers[x],estateName)
            name = raw_input()
            population = self.calculateVillagePopulation()
            print "%s has a population of %d. How many percent of them are indentured? (max 40 percent)" %(name,population)
            indentured = raw_input()
            while indentured.isdigit() == False or int(indentured) > 40 or int(indentured) < 0:
                print "Please type a number between 0 and 40"
                indentured = raw_input()
            land = self.calculateVillageLand(population)
            village = Village(name,int(population), int(indentured),int(land))
            villages.append(village)
            print "Your %s village: " %ordinalNumbers[x]
            village.printInfo()




class Fiefdom:

    def __init__(self):
        self.industries = {}
        self.industries["Farming"] = 1
        self.industries["Livestock"] = 1
        self.industries["Forest"] = 1
        self.industries["Fishing"] = 0
        self.rank = 2 #noble rank 1 = Landed Knight 5 = King/similar
        self.qualityPoints = 25
        self.forestArea = 0 #Acres
        self.estates = []

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
            print "You do not have enough points for that change"
            return self.qualityPoints, cost
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
class Village:

    def __init__(self, name, population, indenturedPercent, land):
        self.indenturedPop = (population*indenturedPercent)/100
        self.freePop = population - self.indenturedPop
        self.name = name
        self.indenturedLand = (land*indenturedPercent)/100
        self.freeLand = land - self.indenturedLand

    def printInfo(self):
        print "%s has a free population of %d people and an indentured population of %d people. It has %d acres of land connected to it." %(self.name, self.freePop, self.indenturedPop, self.freeLand+self.indenturedLand)

class Estate:

    def __init__(self, estateLand):
        self.villages = []
        self.land = estateLand
        self.steward = [dieRoller(1,6)+12,dieRoller(1,6)+12]



factory = FiefdomFactory()
oakheart = Fiefdom()


doingSetup = True

while doingSetup:
    print "Your current industry qualities are:"
    oakheart.printIndustryQualities()
    print "You have %d points left. What would you like to do?" %oakheart.qualityPoints
    printChoices(oakheart.industries)
    choice = raw_input()
    while choice.isdigit() == False:
        print "Please use only numerics"
        choice = raw_input()
    doingSetup = handleInput(choice, oakheart)
    #doingSetup = False

oakheart.estates = factory.buildEstates(oakheart.rank)
