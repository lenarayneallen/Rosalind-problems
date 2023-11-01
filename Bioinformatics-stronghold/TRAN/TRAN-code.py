#transitions and transversion

#function to generate a dictionary of fasta labels
#and sequences from a fasta file
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
file = 'rosalind_tran.txt'
f = open(file)
parsedseqs = parse_file(f)

#generate list of all sequences from the fasta dictionary
parsed_values = parsedseqs.values()
seqs = []
for seq in parsed_values:
    seqs.append(seq)


s1 = seqs[0]
s2 = seqs[1]

#get the length of both sequences
len_each_seq = len(s1)

#function that returns the transition/transversion ratio 
def get_tt_ratio(seq1, seq2):
   
    #set counts for transitions and transversions to 0
    transitions = 0
    transversions = 0
   # iterate through each base in the first sequence
    for i in range(len_each_seq):
        #only proceed if there is a point mutation
        if seq1[i] != seq2[i]:
            #determine if point mutation is a transtion or transversion based on the current base
            
            if seq1[i] == "G":
                if seq2[i] == "A":
                    transitions += 1                
                else:
                    transversions += 1
            if seq1[i] == "C":
                if seq2[i] == "T":
                    transitions += 1                
                else:
                    transversions += 1
            if seq1[i] == "A":
                if seq2[i] == "G":
                    transitions += 1                
                else:
                    transversions += 1
            if seq1[i] == "T":
                if seq2[i] == "C":
                    transitions += 1                
                else:
                    transversions += 1
    return transitions/transversions

print(get_tt_ratio(s1, s2))
