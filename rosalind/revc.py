#!/usr/bin/env python

# reverse complement a DNA sequence

from util import read_input

def complement(x):
    """
    Complement a nucleotide

    Parameters
    ----------
    x : str
        A nucleotide. Should be one of A, C, T, G.

    Returns
    -------
    str
        The complement of the input nucleotide; A=T, G=C, and vice versa. Will return None if the
        input is not valid.
    """
    if x == "A":
        return "T"
    elif x == "T":
        return "A"
    elif x == "G":
        return "C"
    elif x == "C":
        return "G"
    else: # if no valid nucleotide was input
        return None

def complement_sequence(seq):
    """
    Complement a DNA sequence

    Parameters
    ----------
    seq : str
        A DNA sequence.

    Returns
    -------
    str
        The complement of the input sequence.
    """
    complemented = ''
    for base in seq:
        complemented += complement(base)
    return complemented

def reverse_complement(seq):
    """
    Reverse complement a DNA sequence

    Parameters
    ----------
    seq : str
        A DNA sequence.

    Returns
    -------
    str
        The reverse complement of the input sequence.
    """
    return complement_sequence(seq[::-1])


def main():
    raw = read_input('../rosalind_data/rosalind_revc.txt')  # since the file only contains one line, I just need to keep the first line of the list that read_input returns
    dna = raw[0]

    # strategy:
    # 1. reverse the DNA
    # 2. complement the reversed sequence bit by bit
    #   - go over all nucleotides and translate each base to its complement

    rev_complement = reverse_complement(dna)

    print(rev_complement)

if "__name__" == "__main__":
    main()