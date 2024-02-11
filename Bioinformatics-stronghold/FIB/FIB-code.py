
DNA = open('FIB-input.txt')
f = DNA.read()

#splitting the two values in the file into a list of two strings

parsed = f.split(' ')

#assigning each string to its corresponding variable and converting them to integers

months = int(parsed[0])
litterpairs = int(parsed[1])

#setting startingpairs to 1

startingpairs = 1

#calculating total number of breeding rabbit pairs present after n months

def breedingpairs(months):
	#the number of breeding pairs present are the same for the first two months
	#creating list of adult pairs present in the colony each month, starting with the first two months
	
	adultpairs = [startingpairs, startingpairs]
	
	#for every month passed, add last month's number of adult pairs
	#to the number of litterpairs times the number of adult pairs that were present two months prior
	#and append this value to the list of adult pairs
	
	for i in range(2, months+1):
		adultpairs.append((adultpairs[i-1]) + ((adultpairs[i-2]) * litterpairs))
		
	return adultpairs[months]

print(breedingpairs(months - 1))
