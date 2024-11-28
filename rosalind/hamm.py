#!/usr/bin/env python

# calculate Hamming distance between two strings

from util import read_input

raw = read_input("../rosalind_data/rosalind_hamm.txt")
s, t = raw

def hamming(s, t):
    """Calculate Hamming distance (number of differing characters) between two strings.

    Parameters
    ----------
    s : str
        the first string
    t : str
        the second string
    
    Returns
    -------
    int
        the Hamming distance (number of mutations) between the two strings.
    """
    dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dist += 1
    return dist


print(hamming(s, t))