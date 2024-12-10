#!/usr/bin/env python

# find (and translate) all open reading frames in a DNA sequence

from util import read_input

# we can take advantage of all the other tools we have written so far
from revc import reverse_complement
from prot import translate, code

def find_orf_starts(rna):
    """find all start codons in an RNA sequence"""
    starts = []
    for i in range(len(rna)-2):
        if rna[i:i+3] == "AUG":
            starts.append(i)
    return starts

def find_orfs(rna, starts):
    """find all open reading frames in an RNA sequence"""
    orfs = []
    for start in starts:
        orf = ""
        for i in range(start, len(rna), 3):
            codon = rna[i:i+3]
            orf += codon
            if len(codon) < 3:
                break
            if code[codon] == "Stop":
                orfs.append(orf)
    return orfs

def main():
    raw = read_input("../rosalind_data/rosalind_orf.txt")
    dna = ''.join(raw[1:])
    # dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

    # strategy:
    # 1. create forward and backward RNA sequences
    forward = dna.replace("T", "U")
    backward_dna = reverse_complement(dna)
    backward = backward_dna.replace("T", "U")

    # 2. find all start codons in both sequences
    f_starts = find_orf_starts(forward)
    b_starts = find_orf_starts(backward)

    # 3. find all open reading frames in both sequences
    f_orfs = find_orfs(forward, f_starts)
    b_orfs = find_orfs(backward, b_starts)

    # 4. translate all open reading frames and print them
    orfs = f_orfs + b_orfs
    proteins = list()
    for orf in orfs:
        protein = translate(orf)
        if protein not in proteins:
            proteins.append(protein)
            print(protein)

if __name__ == "__main__":
    main()