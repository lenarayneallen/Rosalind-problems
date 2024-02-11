#Given: A protein string of length at most 1000 aa.

#Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
#(Don't neglect the importance of the stop codon in protein translation.)

from functools import reduce


# generate dictionay from codon table
codontable = open('codontable.txt', 'r')
codontable = codontable.read()
splitcodontable = codontable.split()

codondict = {}
for index, element in enumerate(splitcodontable):
	if(index<(len(splitcodontable)-1)):
		if len(element) == 3:
			codondict[element] = splitcodontable[index+1]
		else: 
			continue
        
# open and read amino acid sequence
protein_string = open('MRNA-input.txt')
protein_string = protein_string.read()

#generate a list that contains lists of possible codons
#for each amino acid 

possible_mrna_list = [[k for k, v in codondict.items() if v == protein] for protein in protein_string]
new_possible_mrna_list = possible_mrna_list[:-1]


#count the number of mrna codons in each sublist
counts = [len(i) for i in new_possible_mrna_list]

#find the product of all items in counts
counts_multiplied = reduce(lambda x,y: x*y, counts)

#determine total possible number of rna strings,
#taking stop codons into account
total_numer_rna_strings = counts_multiplied * 3

#formatting the total number of rna strings modulo 1000000
modulo_answer = ((total_numer_rna_strings) % 1000000)
print(modulo_answer)
