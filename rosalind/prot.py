#!/usr/bin/env python

# translate an RNA sequence into protein

from util import read_input

# create a reference dictionary with the genetic code
# read the RNA in triplets
# map triplet to aminoacid

code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

def translate(rna):
    """
    Translate an RNA sequence into protein

    Parameters
    ----------
    rna : str
        An RNA sequence.

    Returns
    -------
    str
        The protein sequence corresponding to the input RNA sequence.
    """
    peptide = ""
    for start in range(0, len(rna), 3):
        codon = rna[start:start+3]
        aminoacid = code[codon]
        if aminoacid == "Stop":
            break
        peptide += aminoacid
    return peptide

def main():
    line_list = read_input("../rosalind_data/rosalind_prot.txt")
    rna = line_list[0]

    peptide = translate(rna)
    print(peptide)


if __name__ == "__main__":
    main()