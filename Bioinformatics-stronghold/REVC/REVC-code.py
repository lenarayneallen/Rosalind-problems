

DNA = open('input.txt')
DNA_string = DNA.read()

#reversing DNA string
rev_DNA_string = DNA_string[::-1]


def reverse_complement(DNA_string):
	complement_dictionary = {"A":"T", "T":"A", "G":"C", "C":"G"}
	complement_string = ""
	for base in DNA_string:
		if base in complement_dictionary:
			complement_string += complement_dictionary[base]
	print (complement_string)

reverse_complement(rev_DNA_string)
