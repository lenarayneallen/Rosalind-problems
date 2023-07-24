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

#open and parse FASTA file, creating a dictionary (parsedseq) where keys = labels, and values = sequences
ff = 'GRPH-input.txt'
f = open(ff)
parsedseq = parse_file(f)

#create an inverted version of parsedseq where keys = sequences and labels = values
inv_parsedseq = dict(zip(parsedseq.values(), parsedseq.keys()))

#initialize a list to hold all sequences and append sequences to this list
seq_list = []
for string in parsedseq.values():
    seq_list.append(string)
    
#initialize a list to hold adjacency list
adj_list = []


#loop over all sequences
for s in seq_list:
    seq = s
    
    #identify the 3-base prefix and suffix of current sequence
    sprefix = seq[:3]
    ssuffix = seq[-3:]
    
    #create list (others) of all other sequences in seq_list besides current sequence
    others = [s for s in seq_list if s != seq]
    
    #loop over all sequences in others 
    for t in others:
        
        #identify the 3-base prefix and suffix of current sequence in others
        tprefix = t[:3]
        tsuffix = t[-3:]
        
        #ensure that the current sequence in seq_list is not equal to the current sequence in others
        if s != t:
            
           #append the labels of the current sequence in seq_list and current sequence in others to adj_list as a tuple
           #if the suffix of the current sequence in seq_list is equal to the prefix of the current sequence in others
            if ssuffix == tprefix:
                adj_list.append((inv_parsedseq[s], inv_parsedseq[t]))
                
                #append the labels of the current sequence in others and current sequence in seq_list to adj_list as a tuple
                #if the suffix of the current sequence in others is equal to the prefix of the current sequence in seq_list
                if tsuffix == sprefix:
                    adj_list.append((inv_parsedseq[t], inv_parsedseq[s]))
        
    

#format and print tuples from adj_list           
for i in adj_list:
    print(str(i[0]) + ' ' + str(i[1]))
