#!/usr/bin/env python

# restriction sites

from util import read_input
from revc import reverse_complement

def reverse_palindrome(seq, pos, length):
    examine = seq[pos:pos+length]
    if reverse_complement(examine) == examine:
        return True
    return False

def main():
    seq = ''.join(read_input('../rosalind_data/rosalind_revp.txt')[1:])
    # seq = 'TCAATGCATGCGGGTCTATATGCAT'
    n = len(seq)
    for window in range(4, 13, 2):
        for i in range(0, n-window+1):
            if reverse_palindrome(seq, i, window):
                print(i+1, window)
    # examine = 'ATGCAT'
    # print(examine, reverse_complement(examine))


if __name__ == "__main__":
    main()