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

input_file = 'consensusex.txt'
f = open(input_file)
parsedseq = parse_file(input_file)

#importing numpy and pandas
import numpy as np 
import pandas as pd

#building a list of sequences from the parsed fasta file
sequences= []
for key, value in parsedseq.items():
	sequences.append(value)

#getting the length of all sequences
#getting the number of sequences in the sequences 
#creating an empty list
seq_length = len(value)
number_of_sequences = len(sequences)
sequences_no_spaces = []

#appending all nucleotides in the sequences list continuously
for i in sequences:
	for base in i:
		sequences_no_spaces.append(base)

#creating numpy arrays of the sequences
#creating empty numpy array for profile matrix
seqarray = np.array(sequences_no_spaces).reshape(number_of_sequences,seq_length)
countarray = np.zeros((4, seq_length), dtype = 'int16')

#creating profile matrix 
x = 0
while x <= seq_length - 1:
	column = seqarray[:, x]
	for i in column:
		if i == 'A':
			countarray[0,x] = countarray[0,x] + 1
		if i == 'C':
			countarray[1,x] = countarray[1,x] + 1
		if i == 'G':
			countarray[2,x] = countarray[2,x] + 1
		if i == "T":
			countarray[3,x] = countarray[3,x] + 1
	x = x + 1

#converting profile matrix to a dataframe
#reformatting index labels 
#creating empty list
df = pd.DataFrame(countarray, index = ['A', 'C','G','T'])
df_index_labels_correct = pd.DataFrame(countarray, index = ['A:','C:','G:','T:'])
mostcommon = []

#identifying most common nucleotides in every dataframe column for consensus sequence
#appending them to empty list
mostcommonframe = df.idxmax()
for c in mostcommonframe:
	mostcommon.append(c)

#formatting dataframe as a string
dfstring = df_index_labels_correct.to_string(header = False)

#removing spaces from consensus sequence
joinedmostcommon =''.join(str(y) for y in mostcommon)


print(joinedmostcommon)
print(dfstring)
