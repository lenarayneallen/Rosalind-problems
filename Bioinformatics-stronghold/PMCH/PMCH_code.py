import math
def parse_file(input_file):

	fasta_dict = {}
	sequence_id = None
	sequence = []

	for line in input_file:
		line = line.strip()

		if line.startswith(">"):
			if sequence_id is not None:
				fasta_dict[sequence_id] = ''.join(sequence)
			sequence_id = line[1:]
			sequence = []
			continue
		sequence.append(line)
	fasta_dict[sequence_id] = ''.join(sequence)
	return fasta_dict

#open file and create dictionary of fasta labels
#and sequences
file = 'rosalind_pmch.txt'
f = open(file)
parsedseqs = parse_file(f)

parsed_values = parsedseqs.values()
seq = ''
for sequence in parsed_values:
    seq =(sequence)


def number_perfect_matchings(s):
    
    #it is given in the problem that there will be the same
    #number of As as Us/ same number of Cs as Gs
    #count the number of As/Gs
    num_of_A_U = s.count('A')
    num_of_G_C = s.count('G')

    #get the number of potential pairings for A/Us and G/Cs 
    #by computing the factorial of each count
    AU_possible_pairings = math.factorial(num_of_A_U)
    GC_possible_pairings = math.factorial(num_of_G_C)

    #get number of perfect matches by multiplying possible 
    #pairings of A/U by the possible pairings of G/C
    perf_match_num = AU_possible_pairings * GC_possible_pairings

    return perf_match_num

print(number_perfect_matchings(seq))
