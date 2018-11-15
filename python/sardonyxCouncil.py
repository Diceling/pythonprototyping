
import nameGenerator as names
import random as rand
import math

stocks = 5000
nrOfSeats = 51



remainingSeats = nrOfSeats
owners = {
	"carwelan": 3501,
	"duncan": 120,
	"celdorion": 140,
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

seatAllocation = {}
stockPower = {}
for k in owners.keys():
	seatAllocation[k] = 0
	stockPower[k] = 0.0


def calculateStockPower(stocks, seats):
	s = seats
	if s == 0:
		s = 1
	v = stocks

	a = v/(s*math.sqrt(s*(s+1)))
	return a

while remainingSeats > 0:
	highestStockPower = 0
	highestOwner = ""
	for k,v in owners.iteritems():
		power = calculateStockPower(v,seatAllocation[k])
		print power, k
		if power > highestStockPower:
			highestStockPower = power
			highestOwner = k
	seatAllocation[highestOwner] = seatAllocation[highestOwner]+1
	remainingSeats = remainingSeats-1

while len(seatAllocation.keys()) > 0:
	mostSeats = 0
	owner = ""
	for k, v in seatAllocation.iteritems():
		if v >= mostSeats:
			mostSeats = v
			owner = k
	print owner, mostSeats
	seatAllocation.pop(owner)
