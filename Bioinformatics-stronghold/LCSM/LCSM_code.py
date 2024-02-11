#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


#parsing fasta file

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

input_file = 'LCSM-input.txt'
f = open(input_file)
parsedseq = parse_file(f)

#creating list of sequences from parsed fasta
sequences= []
for key, value in parsedseq.items():
	sequences.append(value)

#finding sortest sequence, its index, and its length  
shortest = min(sequences, key = len)
shortest_index = sequences.index(shortest)
shortest_length = len(shortest)

#making a list to store all common motifs
list_of_common_motifs = []

#iterating through the shortest sequence to find strings that are common to all sequences
#adding them to the list of common motifs
y = 0
x = 1
while x <= shortest_length:
	seq_of_interest = sequences[shortest_index][y:x]
	if all(seq_of_interest in string for string in sequences) == True: 
		list_of_common_motifs.append(seq_of_interest)
		x = x + 1
	else:
		y = y + 1
		x = y + 1

#printing the longest common motif
print(max(list_of_common_motifs, key = len))
