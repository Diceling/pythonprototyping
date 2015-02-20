#########################
# Basic Python Protoype for a board game Companion to the game Letters From Whitechapel, by Fantasty Flight. 
# Author: Gunnar Södergren
# Company: Street Samurai Studios
# Licensed under GNU GPL
#########################

class Spot:
	
	number = -1
	availableByWalking  = []
	availableByCoach = []
	availableByAlley = []
	
	def __init__(self, abw, abc, aba, num):
		self.number = num
		self.availableByWalking = abw
		self.availableByCoach = abc
		self.availableByAlley = aba
	

	
blacklist = [[],[],[],[]]

allSpots = []

s = Spot([2,4],[],[],1)
allSpots.append(s)
s = Spot([1,3,5],[],[],2)
allSpots.append(s)
s = Spot([2,6],[],[],3)
allSpots.append(s)
s = Spot([1,5,7],[],[],4)
allSpots.append(s)
s = Spot([2,4,6,8],[],[],5)
allSpots.append(s)
s = Spot([3,5,9],[],[],6)
allSpots.append(s)
s = Spot([4,8],[],[],7)
allSpots.append(s)
s = Spot([7,5,9],[],[],8)
allSpots.append(s)
s = Spot([6,8],[],[],9)
allSpots.append(s)

def getPosLocationsForSpot(currSpot):
	for spot in allSpots:
		if(spot.number == currSpot):
			return spot.availableByWalking
	
def getAllPossibleLocations(nbrOfMoves, startingLocation, blacklist):
	possibleCurrLocations = []
	possibleNextLocations = []
	currentSpot = startingLocation
	
	possibleCurrLocations.append(currentSpot)
	for i in range(nbrOfMoves):
		for currLoc in possibleCurrLocations:
			currentSpot = currLoc
			for location in getPosLocationsForSpot(currentSpot):
				possibleNextLocations.append(location)
		possibleCurrLocations = possibleNextLocations
		possibleNextLocations = []
	print possibleCurrLocations
	
getAllPossibleLocations(4,1,[])