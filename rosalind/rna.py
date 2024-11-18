#!/usr/bin/env python

# translate a DNA sequence to RNA

from util import read_input

# read in the data using my utility function
raw_input = read_input('../rosalind_data/rosalind_rna.txt')
dna = raw_input[0]  # since the file only contains one line, I just need to keep the first line of the list that read_input returns

# solution strategy:
# build up RNA string by translating each nucleotide
# if we see a T, write U; else, write the current nucleotide

rna = ''
for nucleotide in dna:
    if nucleotide == 'T':
        rna += 'U'
    else:
        rna += nucleotide

print(rna)

# alternatively, we could just do dna.replace('T', 'U')