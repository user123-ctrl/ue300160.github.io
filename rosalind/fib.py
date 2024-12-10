#!/usr/bin/env python

# calculate the number of rabbit pairs after n months if rabbits have k offspring and a pair of
# rabbits takes one month to mature

from util import read_input

# read in the data
raw_input = read_input('../rosalind_data/rosalind_fib.txt')
n, k = map(int, raw_input[0].split())

# solution strategy:
# (we drew lots of rabbit family trees to figure this out)
# (we can translate the formula into a recursion)

def rabbits(n, k):
    if n < 2:
        return n
    else:
        return rabbits(n - 1, k) + k * rabbits(n - 2, k)
    

print(rabbits(n, k))