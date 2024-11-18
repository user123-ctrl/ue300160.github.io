#!/usr/bin/env python

# count nucleotide frequencies

from util import read_input

file = read_input('../rosalind_data/rosalind_dna.txt')
dna = file[0] # since the file only contains one line, I just need to keep the first line of the list that read_input returns

# strategy:
# make a dictionary that will hold the total counts for all nucleotides
# go over all nucleotides, and increase the counter of each nucleotide when seeing it
# e.g. when we see "A" we will increase the value of counts["A"] by one
counts = {
    'A': 0,
    'T': 0,
    'C': 0,
    'G': 0,
}

for base in dna:
    counts[base] += 1

# output needs to be printed in a certain order:  'A', 'C', 'G', and 'T', and it needs to be in one row
result = ''
for base in ['A', 'C', 'G', 'T']:
    result += str(counts[base]) + ' ' # I need to make sure that counts[base] is converted to a string, because it is a number by nature

# now print the result, but remove the last space
print(result.strip())