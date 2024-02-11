#Given: A DNA string s
 of length at most 1000 bp.
#Return: The reverse complement sc of s

#opening file
DNA = open('REVC-input.txt')
DNA_string = DNA.read()

#reversing DNA string
rev_DNA_string = DNA_string[::-1]

#finding reverse complement using a dictionary 
def reverse_complement(sequence):
	complement_dictionary = {"A":"T", "T":"A", "G":"C", "C":"G"}
	complement_string = ""
	for base in sequence:
		if base in complement_dictionary:
			complement_string += complement_dictionary[base]
	return (complement_string)

print(reverse_complement(rev_DNA_string))
