#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t



#open and read in file
DNA = open ('RNA-input.txt')
DNA_string = DNA.read()
#replace all instances of thymine with uracil
RNA = DNA_string.replace('T','U')
print(RNA)
