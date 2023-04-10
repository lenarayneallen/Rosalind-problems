DNA = open('githubfib.txt')
f = DNA.read()

parsed = f.split(' ')

months = int(parsed[0])
litterpairs = int(parsed[1])
startingpairs = 1

def breedingpairs(months):
	adultpairs = [startingpairs, startingpairs]
	for i in range(2, months+1):
		adultpairs.append((adultpairs[i-1]) + ((adultpairs[i-2]) * litterpairs))
	return adultpairs[months]

print(breedingpairs(months - 1))
