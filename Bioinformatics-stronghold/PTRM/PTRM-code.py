#Given: A protein string P of length at most 1000 aa.
#Return: The total weight of P. Consult the monoisotopic mass table.


#import monoisotopic mass table
f = open('masstable.txt', 'r')
masstable = f.read()
splitmasstable = masstable.split()

massdict = {}

#format as dictionary
for index, element in enumerate(splitmasstable):
	if(index<(len(splitmasstable)-1)):
		if len(element) == 1:
			massdict[element] = splitmasstable[index+1]
		else:
			continue
#open file conatining protein string        
s = open('PTRM-input.txt', 'r')
p = s.read().strip()

#create a list containing each amino acid's 
#corresponding mass
mass_list = []
for aa in p:
    mass_list.append(float(massdict[aa]))
    
#sum the corresponding masses from the list created above
total_weight = sum(mass_list)

print(total_weight)
