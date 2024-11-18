#!/usr/bin/env python

from util import read_input

# first, read the file!
test = "../rosalind_data/ini5.txt"
lines = read_input(test)
# with open(filepath, 'r') as infile:
#     lines = infile.readlines()
#     for line in lines:
#         print(line.strip())

for l in lines[1::2]:
    print(l.strip())

