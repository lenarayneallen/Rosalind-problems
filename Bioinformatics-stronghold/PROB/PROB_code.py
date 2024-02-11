#Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

#Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k]
#will match s exactly.


import math
#read in file
s = open('PROB_input.txt', 'r')
p = s.read()
psplit = p.split()


#isolate sequence
seq = psplit[0]

#isolate GC content array and convert from strings to integers
GC_array = psplit[1:]
GC_arr_int = [eval(i) for i in GC_array]

def calc_GC_prob(s, gc_arr):
#count number of A/Ts and G/Cs in sequence
    AT_count = 0
    GC_count = 0
    for base in s:
        if base == 'A' or base == 'T':
            AT_count += 1
        else:
            GC_count += 1

    #initialize empty lists to store probabilities for each GC content value
    AT_prob = []
    GC_prob = []

    #iterate through array of GC contents and calculate 
    #probabilities that a string of the given GC content will 
    #have the same number of AT's / GC's as s
    for i in gc_arr:
        AT_prob.append(math.log10(((1-i)/2)**AT_count))
        GC_prob.append(math.log10((i/2)**GC_count))

    #caluclate probability that a random string with given GC content
    #matches s, given that log10(x*y) = log10(x) + log10(y)
    B = [AT_prob[i] + GC_prob[i]for i in range(len(gc_arr))]   

    #round floats to three decimal places
    rounded_B = ['%.3f' % i for i in B]

    return rounded_B

log10_probabilities = calc_GC_prob(seq, GC_arr_int)
print(*log10_probabilities)
