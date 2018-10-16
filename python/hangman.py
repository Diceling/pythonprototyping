import random as rand
import copy


file = open ('words_alpha.txt','r')
lines = file.readlines()
file.close()

words = []
for line in lines:
	words.append(line.rstrip())


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def eliminateWrongAmount(remainingWords, puzzle):
	returnWords = []
	for word in remainingWords:
		if len(word) == len(puzzle):
			returnWords.append(word)
	
	return returnWords

def doesNotContainLetter(remainingWords, letter):
	returnWords = []
	for word in remainingWords:
		if letter not in word:
			returnWords.append(word)
	return returnWords

def containsLetter(remainingWords, lettersKnown):
	returnWords = []
		
	for word in remainingWords:
		possibleWord = True
		for x in range(0, len(lettersKnown)):
			if lettersKnown[x] == "*":
				continue
				
			if word[x] != lettersKnown[x]:
				possibleWord = False
				break
			
		if possibleWord:
			returnWords.append(word)
		
	return returnWords

def calculateGuess(remainingWords, guesses):
	guessDict = {}
	for guess in guesses:
		guessDict[guess] = 0
	for key in guessDict.keys():
		for word in remainingWords:
			for letter in word:
				if letter == key:
					guessDict[key]= guessDict[key]+1
	
	highestKey = ""
	highestNumber = 0
	for k,v in guessDict.iteritems():
		if v >= highestNumber:
			highestKey = k
			highestNumber = v
	return highestKey
	
	


	
runs = 1000
sumGuesses = 0
avg = 1.0
minGuesses = 40
maxGuesses = 0
for x in range(0,runs):
	chosenWord = words[rand.randint(0,len(words))]
	guessesLeft = copy.copy(alphabet)

	known = []

	print "Word is: %s, a %d-letter word" %(chosenWord, len(chosenWord))

	for letter in chosenWord:
		known.append("*")
		
	## Setup
	wordsLeft = copy.copy(words)

	wordsLeft = eliminateWrongAmount(wordsLeft, chosenWord)
	#print "Words left: %d out of %d" % (len(wordsLeft), len(words))
	guessNr = 0
	while "*" in known:
		guess = calculateGuess(wordsLeft, guessesLeft)
		if guess == "":
			break
		guessNr = guessNr+1
		#print "Guess Nr %d is: %s" % (guessNr, guess)
		
		nrOfOccurences = 0
		for x in range(0, len(chosenWord)):
			if chosenWord[x] == guess:
				known[x] = guess
				nrOfOccurences = nrOfOccurences+1
		if nrOfOccurences > 0:
			wordsLeft = containsLetter(wordsLeft,known)
		else:
			wordsLeft = doesNotContainLetter(wordsLeft, guess)
		guessesLeft.remove(guess)
		#print "Nr of words left after guess %d: %d" % (guessNr,len(wordsLeft))
		if len(wordsLeft) <=1:
			for x in range(0,len(known)):
				if known[x] == "*":
					known[x] = wordsLeft[0][x]
		#print known
	#print ""
	word = "".join(known)
	sumGuesses = sumGuesses +1
	if guessNr > maxGuesses:
		maxGuesses = guessNr
	if guessNr < minGuesses:
		minGuesses = guessNr
	if word == chosenWord:
		print "The Word is %s and I got it in %d guesses" % (word, guessNr)
	else:
		print "I failed!"

avg = float(sumGuesses)/float(runs)
print "I ran %d games and these are the stats:" %runs
print "Average: %f" % avg
print "Max: %d" % maxGuesses
print "Min: %d" % minGuesses

	

