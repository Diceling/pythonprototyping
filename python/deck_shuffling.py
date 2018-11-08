import random as rand 
import copy


def getSuitedDeck():
	suits = ["H","S","C","D"]
	deck = []

	for s in suits:
		for x in range(1,14):
			deck.append("%s%d" % (s,x))
	return deck
	
def getNumberedDeck():
	for x in range(1,53):
			deck.append(x)
	return deck


def riffle(_deck):
	cut = rand.randint(20,30)
	topHalf = _deck[:cut]
	bottomHalf = _deck[cut:]
	shuffledDeck = []
	currentHalf = 1
	counter = 0
	while len(topHalf) > 0 or len(bottomHalf) > 0:
		counter = counter+1
		if currentHalf == 1:
			shuffledDeck.insert(0,topHalf.pop())
		else:
			shuffledDeck.insert(0, bottomHalf.pop())
		
		for x in range(0,counter):
			switch = rand.randint(1,2)
			if currentHalf != switch:
				currentHalf = switch
				counter = 0
				break
		if currentHalf == 1 and len(topHalf) == 0:
			currentHalf = 2
		if currentHalf == 2 and len(bottomHalf) == 0:
			currentHalf = 1
	return shuffledDeck

def calculateRandomnessScore(_deck):
	score = 0
	for x in range(0, len(_deck)):
		if deck[x] != x+1:
			score = score + 1
		if x > 0 and _deck[x] != _deck[x-1]+1:
			score = score+1
		if x < len(deck)-1 and _deck[x] != _deck[x+1]-1:
			score = score+1
	return score
		
	
	
deck =[]
deck = getNumberedDeck()
for x in range(0,7):
	deck = riffle(copy.deepcopy(deck))
	print calculateRandomnessScore(deck)
print deck
