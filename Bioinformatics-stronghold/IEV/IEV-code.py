#open file and create list of integers corresponding to 
#number of couples of each genotype pairing 
s = open('iev.txt', 'r')
p = s.read()
integers = p.split()


#create dictionary where keys correspond to genotype pairing 
#and values correspond to the expected number of offspring for 
#each genotype pairing subpopulation given that each couple has
#one offspring
genotype_dict = {'AA-AA': float(integers[0] * 1), 'AA-Aa' : float(integers[1] * 1),
                 'AA-aa': float(integers[2] * 1), 'Aa-Aa' : float(integers[3]) * 0.75,
                 'Aa-aa': float(integers[4]) * 0.5, 'aa-aa' : float(0)}

#initialize list and append expected numbers of 
#offspring displaying the dominant phenotype for each subpopulation
numlist = []
for val in genotype_dict.values():
        numlist.append(val)

#sum the expected numbers of offspring displaying the
#dominant phenotype for each subpopulation, and multiply
#final answer by 2 to account for each couple having 
#two offspring
total_exp_dom_offspring = sum(numlist) * 2
    


print(total_exp_dom_offspring)
