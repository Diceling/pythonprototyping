import itertools

nrOfDice = 6
nrOfSides = 2

outcomes = []

sidesAndNr = {}

sidesAndNr[8] = 2
sidesAndNr[6] = 5

def addDice(currOutcomes, dice):
    array = []

    newOutcomes = []
    for x in currOutcomes:
        for y in range(1,dice+1):
            newOutcomes.append("%s,%d" %(x,y))


    return newOutcomes

def fetchRolls(diceDict):
    allOutcomes = ["R"]

    for sides, nr in diceDict.iteritems():
        for x in range(0,nr):
            allOutcomes = addDice(allOutcomes, sides)
    for x in range(0, len(allOutcomes)):
        allOutcomes[x] = allOutcomes[x][2:]
    return allOutcomes

def fetchOutcomes(rolls):
    outcomes = {}
    for x in rolls:
        rollSum = sum(map(int, x.split(",")))
        if rollSum not in outcomes:
            outcomes[rollSum] = 1
        else:
            outcomes[rollSum] = outcomes[rollSum]+1
    return outcomes


rolls = fetchRolls(sidesAndNr)
outcomes = fetchOutcomes(rolls)
for k,v in outcomes.iteritems():
    print "Outcome: %d, Number: %d Chance: %f" % (k,v, (float(v)/float(len(rolls)))*100)
