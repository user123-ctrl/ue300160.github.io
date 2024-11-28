#!/usr/bin/env python

# find a motif in a string

from util import read_input

raw = read_input('../rosalind_data/rosalind_subs.txt')
s = raw[0]
t = raw[1]
# s = "GATATATGCATATACTT"
# t = "ATAT"

# solution strategy:
# iterate through the string s in a rolling window and check if the substring matches t
# this is useful, so we should write it down as a function

def find_motif(s, t):
    motif = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            motif.append(i)
    return motif

motif_locs = find_motif(s, t)

# rosalind wants us to print in human-readable mode, so I need to add 1 to each location/index
result = ''
for loc in motif_locs:
    result += str(loc + 1) + ' '
print(result)