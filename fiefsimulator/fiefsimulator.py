import random as rand

availableIndustries = ["Farming", "Fishing", "Forest", "Livestock", "Hunting"]
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
            points, cost = fief.changeIndustryQuality(availableIndustries[int(choice)-1],int(newValue))
            print "That change cost: %d. You now have %d points left" %(cost, points)
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
        self.forestArea = forestQuality*dieRoller(3,6,True)*10
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
        print "You have %d estates in your fiefdom." %nrOfestates
        for i in range(nrOfestates):
            print "What would you like to name your %s estate" %ordinalNumbers[i]
            name = raw_input()
            estLand = self.calculateEstateLand()
            villages = []
            villages = self.buildVillages(self.calcNrOfVillages(), name)
            estates.append(Estate(estLand,villages))
        return estates

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
            print "%s %s village: " %(estateName, ordinalNumbers[x])
            village.printInfo()
        return villages

class FiefdomHandler:

    def __init__(self):
        print "Created Fiefdomhandler"

    def divideEstateLand(self,fief):
        totalEstateLand = 0
        for x in fief.estates:
            totalEstateLand = totalEstateLand + x.land
        print "Your fief has a total of %d acres of estate land. This can be used for either farming och livestock. A third must be used for each, and it can be changed each year." %totalEstateLand
        print "How much would you like to use for farming?"
        farmLand = raw_input()
        while farmLand.isdigit() == False or int(farmLand) > 2*totalEstateLand/3 or int(farmLand) < totalEstateLand/3:
            print "Please use only digits and type a value bigger than %d and smaller than %d" %(totalEstateLand/3, (2*totalEstateLand/3))
            farmLand = raw_input()
        livestockLand = totalEstateLand-int(farmLand)
        return int(farmLand),livestockLand
    def decideDayLabours(self,fief):
        print "Your farmers owe you a number of day labours. The amount of day labours you demand directly affects their ability to work properly, their loyalty towards you and their likelihood to rebel."
        print "40 day labours per farmer is considered Kind, and lowers the difficulty of all farmer-related rolls by one step."
        print "80 day labours per farmer is considered Fair, and does not affect the difficulty of farmer-related rolls"
        print "120 day labours per farmer is considered Hard, and increases the difficulty of all farmer-related rolls by one step."
        print "160 day labours per farmer is considered Harsh, and increases the difficulty of all farmer-related rolls by two step."
        print "200 day labours per farmer is considered Cruel, and increases the difficulty of all farmer-related rolls by three step."
        print "How many day labours will you demand of your farmers?"
        labours = raw_input()
        while labours.isdigit() == False or int(labours) > 200:
            print "Please type a digit lower than 200."
            labours = raw_input()
        level = int(labours)/40-2
        return int(labours), level

    def calculatePotentialIncomes(self, fief):
        taxes = 0
        indenturedPayments = 0
        ownFarming = fief.farmArea*fief.industries["Farming"]
        ownLivestock = fief.livestockArea*fief.industries["Livestock"]
        ownHunting = fief.industries["Hunting"]*fief.forestArea/10


        for estate in fief.estates:

            for village in estate.villages:
                taxes = taxes+0.1*village.freeLand*0.5*fief.industries["Farming"]
                indenturedPayments = indenturedPayments+0.25*village.indenturedLand*0.5*fief.industries["Livestock"]

        incomes = {}
        incomes["Indentured Villagers"] = indenturedPayments
        incomes["Taxation"] = taxes
        incomes["Estate Farming"] = ownFarming
        incomes["Estate Livestock"] = ownLivestock
        incomes["Hunting"] = ownHunting

        return incomes






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
        self.livestockArea = 0
        self.farmArea = 0
        self.estates = []
        self.farmerDifficulty = 0
        self.totalDayLabours = 0

    def changeIndustryQuality(self, industry, newValue):
        cost = 0
        currValue = self.industries[industry]
        if newValue > self.industries[industry]:
            for x in range(newValue,currValue,-1):
                cost = cost+x
        else:
            for x in range(currValue,newValue,-1):
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
    def setEstateLandUse(self, landUse):
        self.farmArea = landUse[0]
        self.livestockArea = landUse[1]

    def calculateDayLabours(self, labourData):
        self.totalDayLabours = labourData[0]*self.getNrOfVillagers()
        self.farmerDifficulty= self.farmerDifficulty+labourData[1]

    def getNrOfVillagers(self):
        totalNrOfVillagers = 0
        for est in self.estates:
            for vill in est.villages:
                totalNrOfVillagers = totalNrOfVillagers+ vill.indenturedPop+vill.freePop
        return totalNrOfVillagers
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

    def __init__(self, estateLand, villages):
        self.villages = villages
        self.land = estateLand
        self.steward = NPC()
        self.steward.skills["Agriculture"] = dieRoller(1,6)+12
        self.steward.skills["Animal Handling"] = dieRoller(1,6)+12



factory = FiefdomFactory()
handler = FiefdomHandler()
oakheart = Fiefdom()

class NPC:

    def __init__(self):
        self.skills = {}


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

#BuildingEstate
oakheart.estates = factory.buildEstates(oakheart.rank)
oakheart.forestArea = factory.calculateForestArea(oakheart.industries["Forest"])

#Initial Setup for first year
oakheart.setEstateLandUse(handler.divideEstateLand(oakheart))
oakheart.calculateDayLabours(handler.decideDayLabours(oakheart))
incomes = handler.calculatePotentialIncomes(oakheart)
print "Potential incomes from your fiefdom:"
for k,v in incomes.iteritems():
    print "%s: %s" %(k,v)
