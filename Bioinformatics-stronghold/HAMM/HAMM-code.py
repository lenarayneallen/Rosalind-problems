#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t)

#opening file and separating by spaces into list
DNA = open('HAMM-input.txt')
f = DNA.read()
twostrings = f.split()

#separating list into strings
s = twostrings[0]
t = twostrings[1]

#counting mismatches
count = 0 
for i in range(len(stra)):
	if s[i] == t[i]:
		continue
	else:
		count = count + 1

print(count)
