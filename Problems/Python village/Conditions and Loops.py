# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

a = 4740
b = 8860
c = 0
for i in range(a, b + 1):
	if i % 2 == 1:
		c = c + i
print (c)
