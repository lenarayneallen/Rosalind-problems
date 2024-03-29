#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


s = open('DNA-input.txt')
dna = s.read()

count_a = 0
count_c = 0
count_g = 0
count_t = 0

for letter in dna:
	if letter == 'A':
		count_a = count_a + 1
	elif letter == 'C':
		count_c = count_c + 1
	elif letter == 'G':
		count_g = count_g + 1
	elif letter == 'T':
		count_t = count_t + 1

print (str(count_a) + ' ' + str(count_c) + ' ' + str(count_g) + ' ' + str(count_t))
