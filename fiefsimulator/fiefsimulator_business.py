import json
import fiefsimulator_dao as dao


def initialize():
    dao.initialize()


def updateIndustries(jsonString):
    jsonDict = json.loads(jsonString)
    remainingPoints = jsonDict["points"]
    currentValues = jsonDict["currentValues"]
    newValues = jsonDict["newValues"]
    totalCost = 0
    for k,v in currentValues.iteritems():
        totalCost = totalCost+calculateCost(v, newValues[k])
    if totalCost <= remainingPoints:
        print "Total cost: %d" %totalCost
        dictionary = {}
        dictionary["id"] = jsonDict["id"]
        dictionary["industries"] = newValues
        dao.updateIndustries(dictionary)
    else:
        print "Not enough points"



def calculateCost(curr, new):
    cost = 0
    if curr == new:
        return 0
    elif curr < new:
        for x in range(curr+1, new+1):
            cost = cost +x
        return cost
    else:
        for x in range(curr, new, -1):
            cost = cost+x
        cost = cost*-1
        return cost
