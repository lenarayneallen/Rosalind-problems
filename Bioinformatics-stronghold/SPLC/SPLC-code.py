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
file = 'splice3.txt'
f = open(file)
parsedseqs = parse_file(f)

#generate list of all sequences from the fasta dictionary
parsed_values = parsedseqs.values()
seqs = []
for seq in parsed_values:
    seqs.append(seq)

#define the DNA sequence and create 
#separate list of introns
dna_string = seqs[0]
introns = []
for x in range(1,len(seqs)):
    introns.append(seqs[x])
    
#delete introns from DNA sequence, leaving only exons
for intron in introns:
    dna_string = dna_string.replace(intron, "")

#transcribe to RNA
rna_exon = dna_string.replace('T','U')

#separate RNA string into codons
n = 3
groups_of_three = []
for i in range(0, len(rna_exon), n):
	groups_of_three.append(rna_exon[i:i+n])

#using codon dictionary, translate exons to protein sequence
aa_string = ""
for codon in groups_of_three:
    aa_string += codondict[codon]

#remove stop codon
aa_string = aa_string.replace("Stop", "")

print(aa_string)
