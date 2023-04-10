DNA = open ('input.txt')
DNA_string = DNA.read()
RNA = DNA_string.replace('T','U')
print(RNA)
