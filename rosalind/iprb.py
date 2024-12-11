#!/usr/bin/env python

# mendel's first law
from util import read_input

def main():
    raw = read_input("../rosalind_data/rosalind_iprb.txt")[0]
    k = int(raw.split()[0])
    m = int(raw.split()[1])
    n = int(raw.split()[2])
    # k = m = n = 2

    S = k + m + n
    prob_dominant = k/S +\
    m/S * (4*k + 3*m -3 + 2*n) / (4*(S-1)) +\
    n/S * (2*k + m) / (2*(S-1))

    print(prob_dominant)

if __name__ == "__main__":
    main()