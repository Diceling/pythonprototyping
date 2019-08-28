import time


primes = []

primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)

x = 9

shouldNot = []
counter = 0
previousPrimes = len(primes)
t0 = time.time()
while len(primes) < 20000:
    counter=counter+1
    if counter%10000 == 0:
        print "%d: %d (%d)" % (counter, len(primes), len(primes)-previousPrimes)
        previousPrimes = len(primes)
    isPrime = True
    x= x+2
    if int(repr(x)[-1]) == 5:
        isPrime = False
        continue
    if sum(map(int, str(x)))%3 == 0:
        isPrime = False
        continue
    g=1
    for i in range(len(primes)-g):
        for j in range(len(primes)-g,i):
            if primes[j]*primes[i] > x:
                g= g+1
            else:
                break
        if x%primes[i] == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(x)
t1 = time.time()

print primes[len(primes)-1]
print t1-t0
