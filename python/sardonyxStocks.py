import random as rand
stocks = 5000
spots = 51

consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","w","z"]
vowels = ["a","e","i","o","u","y"]



owners = {
	"carwelan": 4900,
	"duncan": 50,
	"celdorion": 5,
	"donatella": 5,
	"rowan": 10,
	"nirwe": 10,
	"edna": 10,
	"marcella": 10
}



while sum(owners.values()) < stocks:
	remainingStocks = stocks - sum(owners.values())
	newOwner = ""
	newOwner = consonants[rand.randint(0,len(consonants)-1)]
	newOwner = newOwner + vowels[rand.randint(0,len(vowels)-1)]
	cons = consonants[rand.randint(0,len(consonants)-1)]
	newOwner = newOwner + cons
	newOwner = newOwner + cons
	newOwner = newOwner + vowels[rand.randint(0,len(vowels)-1)]
	
	availableStocks = 0
	if remainingStocks > 50:
		availableStocks = remainingStocks/10
	else:
		availableStocks = remainingStocks
	owners[newOwner] = rand.randint(1,availableStocks)

print owners
spotAllocator = owners.copy()
spotDivision = owners.copy()



for k in spotDivision:
	spotDivision[k] = 0

while spots > 0: 
	maxOwner = ""
	maxStocks = 0
	for key, value in spotAllocator.iteritems():
		if value >= maxStocks:
			maxStocks = value
			maxOwner = key
	spotDivision[maxOwner] = spotDivision[maxOwner]+1
	spotAllocator[maxOwner] = spotAllocator[maxOwner]/2
	spots = spots-1

deleteList = owners.copy()
while len(deleteList) >0:
	highestSpots = 0
	highestOwner = ""
	for k,v in deleteList.iteritems():
		if v >= highestSpots:
			highestSpots = v
			highestOwner = k
	print "%s - %d spots for %d stocks" % (highestOwner, spotDivision[highestOwner], owners[highestOwner])
	deleteList.pop(highestOwner)



