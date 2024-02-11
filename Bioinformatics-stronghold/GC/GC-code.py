#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

input_file = 'GC-input.txt'
f = open(input_file)
parsedseq = parse_file(input_file)

#calculating GC content of each sequence (value) in the dictionary
for aaa,bbb in parsedseq.items():
	totalbases = len(bbb)
	gccount = 0
	for base in bbb:
		if base == 'G':
			gccount = gccount + 1	
		elif base == 'C':
			gccount = gccount + 1
	gcpercent = gccount / totalbases
	#replacing the raw sequence (value) in the dictionary with the GC content
	parsedseq[aaa] = gcpercent

#finding the highest GC content and corresponding key
max_gc = max(parsedseq.values())
max_key = max(parsedseq, key=parsedseq.get)

print(max_key)
print(max_gc * 100)
