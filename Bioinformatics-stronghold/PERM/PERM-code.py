#Given: A positive integer n≤7
#Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

from itertools import permutations

#open file and assign value to n
s = open('PERM-input.txt', 'r')
p = s.read()
n = int(p)

#initialize empty list
num_list = []

#append values of 1 to n+1 to empty list
for i in range(1, n+1):
    num_list.append(i)


#use permutations function from itertools to generate 
#a permutations object containing all permutations of numbers from 1 
#to n as tuples 
perms = permutations(num_list)

#convert the permutations object to a list of tuples
perms_list = list(perms)


#print the length of the list of tuples,
#giving the number of possible permutations
print(len(perms_list))

#print each permutation
for perm in perms_list:
    print(*perm)
