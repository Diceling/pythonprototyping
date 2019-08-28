
import nameGenerator as names
import random as rand
import math

stocks = 5000
nrOfSeats = 51



remainingSeats = nrOfSeats
owners = {
	"builderchairwoman": 1201,
	"eldorion": 801,
	"treville": 400
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
	v = stocks
	divisor = (s*math.sqrt(s*(s+1)))
	if divisor == 0:
		divisor = 1
	a = v/divisor
	return a

while remainingSeats > 0:
	highestStockPower = 0
	highestOwner = ""
	for k,v in owners.iteritems():
		power = calculateStockPower(v,seatAllocation[k])
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
