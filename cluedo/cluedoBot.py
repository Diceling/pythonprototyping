class Card:
    def __init__(self, id, type, name):
        self.id = id
        self.type = type
        self.name = name


class Player:
    def __init__(self, nrOfCards, name):
        self.nrOfCards = nrOfCards
        self.name = name
        self.ownedCards = []
        self.notOwnedCards = []
        self.potentialCards = []
    def addCardToNotOwned(card):
        if card not in self.notOwnedCards:
            self.notOwnedCards.append(card)
    def addToOwnedCards(card):
        if card not in self.ownedCards:
            self.ownedCards.append(card)
    def cleanUp():
        for card in self.notOwnedCards:
            if card in self.potentialCards:
                self.potentialCards.remove(card)
        for card in self.ownedCards:
            if card in self.potentialCards:
                self.potentialCards.remove(card)

class Guess:
    def __init__(self, loc, suspect, wpn, asker, shower, cardShown):
        self.asker = asker
        self.shower = shower
        self.location = loc
        self.suspect = suspect
        self.weapon = weapon
        self.cardShown = cardShown


cardsMasterList = {}
cardsMasterList["Hall"] =  Card(0,"Location", "Hall")
cardsMasterList["Lounge"] =  Card(1,"Location", "Lounge")
cardsMasterList["Dining Room"] =  Card(2,"Location", "Dining Room")
cardsMasterList["Kitchen"] =  Card(3,"Location", "Kitchen")
cardsMasterList["Ballroom"] =  Card(4,"Location", "Ballroom")
cardsMasterList["Conservatory"] =  Card(5,"Location", "Conservatory")
cardsMasterList["Billiards"] =  Card(6,"Location", "Billiards")
cardsMasterList["Library"] =  Card(7,"Location", "Library")
cardsMasterList["Study"] =  Card(8,"Location", "Study")
cardsMasterList["Miss Scarlet"] =  Card(9,"Suspect", "Miss Scarlet")
cardsMasterList["Professor Plum"] =  Card(10,"Suspect", "Professor Plum")
cardsMasterList["Mrs. Peacock"] =  Card(11,"Suspect", "Mrs. Peacock")
cardsMasterList["Rev. Green"] =  Card(12,"Suspect", "Rev. Green")
cardsMasterList["Colonel Mustard"] =  Card(13,"Suspect", "Colonel Mustard")
cardsMasterList["Mrs. White"] =  Card(14,"Suspect", "Mrs. White")
cardsMasterList["Candlestick"] =  Card(15,"Weapon", "Candlestick")
cardsMasterList["Dagger"] =  Card(16,"Weapon", " Dagger")
cardsMasterList["Lead Pipe"] =  Card(17,"Weapon", "Lead Pipe")
cardsMasterList["Revolver"] =  Card(18,"Weapon", "Revolver")
cardsMasterList["Rope"] =  Card(19,"Weapon", "Rope")
cardsMasterList["Spanner"] =  Card(20,"Weapon", "Spanner")

players = []
guesses = []

innocentCards = []
guiltyCards = []

#1. Add a guess to the list
#2. Add guessed cards to notOwnedCards of players who did not show.
#3. Loop through all guesses
#3A. For each guess, check if potentialCards can be eliminated or confirmed from each player. Do this for every player
#4. Repeat 3 and 3A until no information is updated.
#5. Check how many potential combinations are still valid
#6. Repeat.


def newGuess(location, suspect, weapon, asker, shower, cardShown):

    guess =  Guess(location, suspect, weapon, asker, shower, cardShown)

    if cardShown == None:
        players[shower].potentialCards.append(location)
        players[shower].potentialCards.append(suspect)
        players[shower].potentialCards.append(weapon)
    else:
        players[shower].ownedCards.append(cardShown)


    didNotShow = []

    if asker < shower:
        for i in range(asker+1, shower):
            didNotShow.append(i)
    else:
        for i in range(asker+1, len(players)):
            didNotShow.append(i)
        for i in range(0, asker):
            didNotShow.append(i)
    for x in didNotShow:
        players[x].addCardToNotOwned(suspect)
        players[x].addCardToNotOwned(location)
        players[x].addCardToNotOwned(weapon)
        players[x].cleanUp()

def managePlayerCards():
    for x in range(0, len(players)):
        for y in range(0, len(players)):
            if x != y:
                for card in players[x].ownedCards:
                    players[y].addCardToNotOwned(card)

def manageGuesses():
    for guess in guesses:
        if guess.cardShown == None:
            if guess.suspect in players[guess.shower].notOwnedCards and guess.weapon in players[guess.shower].notOwnedCards:
                players[guess.shower].addToOwnedCards(guess.location)
                cardShown = guess.location

            elif guess.suspect in players[guess.shower].notOwnedCards and guess.location in players[guess.shower].notOwnedCards:
                players[guess.shower].addToOwnedCards(guess.weapon)
                cardShown = guess.weapon

            elif guess.location in players[guess.shower].notOwnedCards and guess.weapon in players[guess.shower].notOwnedCards:
                players[guess.shower].addToOwnedCards(guess.suspect)
                cardShown = guess.suspect
def updateGuiltyCheck():

    for card in cardsMasterList:
        innocent = None
        if card not in innocentCards and card not in guiltyCards:
            for player in players:
                if card in player.ownedCards:
                    innocent = True
                    innocentCards.append(card)
                    break
    for card in cardsMasterList:
        if card not in innocentCards:
            guilty = True
            for player in players:
                if card not in player.notOwnedCards:
                    guilty = False
                    break
            if guilty == True:
                guiltyCards.append(card)
