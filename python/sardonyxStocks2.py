import random as rand
import nameGenerator as names

stocks = 5000
spots = 51


levels = [
			stocks*0.025, # 125
			stocks*0.100, # 500
			stocks*0.148, # 740
			stocks*0.297, # 1485
			stocks*0.594  # 2970
]


owners = {
	"carwelan": 1501,
	"duncan": 1200,
	"celdorion": 540,
	"donatella": 200,
	"rowan": 210,
	"nirwe": 52,
	"edna": 102,
	"marcella": 80
}



while sum(owners.values()) < stocks:
	remainingStocks = stocks - sum(owners.values())
	
	
	availableStocks = 0
	if remainingStocks > 50:
		availableStocks = remainingStocks/10
	else:
		availableStocks = remainingStocks
	owners[names.getName()] = rand.randint(1,availableStocks)

print owners
spotAllocator = owners.copy()
spotDivision = owners.copy()



for k in spotDivision:
	spotDivision[k] = 0
	
multiplier = 0
for level in reversed(levels):
	multiplier =  multiplier+1
	for key, value in owners.iteritems():
		if value >= level:
			print "Kick it"
			spotDivision[key] = spotDivision[key]+multiplier
			spots = spots - multiplier
print spots

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
print ""


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


