#Given: A positive integer n (3≤n≤10000).

#Return: The number of internal nodes of any unrooted binary tree having n leaves.

s = open('INOD_input', 'r')
p = s.read()
n = int(p)

internal_nodes = n - 2

print(internal_nodes)
