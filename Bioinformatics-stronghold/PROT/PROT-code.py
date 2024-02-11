#given: an RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#return: the protein string encoded by s.

#open file of RNA sequence
input_file = 'PROT-input.txt'
s = open(input_file, "r")
s = s.read()

#strip newlines
sstripped = s.strip("\n")

#separate RNA bases into groups of three
n = 3
groups_of_three = []
for i in range(0, len(sstripped), n):
	groups_of_three.append(sstripped[i:i+n])


#open and parse codon table file 
codontable = open('codontable.txt', 'r')
codontable = codontable.read()
splitcodontable = codontable.split()

#create dictionary of codons and corresponding amino acids
codondict = {}
for index, element in enumerate(splitcodontable):
	if(index<(len(splitcodontable)-1)):
		if len(element) == 3:
			codondict[element] = splitcodontable[index+1]
		else:
			continue

#create empty string for the amino acid string
aminoacidstring = ""

#append amino acids to empty string
for i in groups_of_three:
	aminoacidstring += codondict[i]

#remove 'stop' at end of string
aminoacidstring = aminoacidstring[:-4]


print(aminoacidstring)

