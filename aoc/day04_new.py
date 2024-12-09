#!/usr/bin/env python

# elf crossword puzzles

from util import read_input

def find_horizontal(word, text):
    total_occurrences = 0
    for line in text:
        total_occurrences += line.count(word)
    return total_occurrences

# finding vertical matches:
# flip the text,
# search for horizontal matches in the flipped text

# function that transposes a text
# so that every row is a column, and vice versa
def flip(text):
    # the trick was to swap the indices
    columns = [''] * len(text) # len(text) is the number of rows we currently have
    for line in text:
        # we have to go over all characters in this line
        # and put each character in its corresponding row in the flipped text
        for i, letter in enumerate(line):
            columns[i] += letter
    return columns

def find_vertical(word, text):
    flipped = flip(text)
    occ = find_horizontal(word, flipped)
    return occ

def dr_diag_starts(n):
    # find all the starting positions for diagonals
    # that go downwards and to the right
    diags = []
    for i in range(n):
        diags.append([i, 0])
    for j in range(1, n):
        diags.append([0, j])
    return diags
    
def dr_diag(text, start):
    i = start[0]
    j = start[1]
    n = len(text)
    diag = ''
    while i < n and j < n:
        diag += text[i][j]
        i += 1
        j += 1
    return diag

def find_diagonal_dr(word, text):
    dr_starts = dr_diag_starts(len(text))
    dr_diagonals = []
    for start in dr_starts:
        diagonal = dr_diag(text, start)
        dr_diagonals.append(diagonal)
    occ = find_horizontal(word, dr_diagonals)
    return occ 

def mirror(text):
    mirrored = []
    for line in text:
        mirrored.append(line[::-1])
    return mirrored

def find_diagonal_dl(word, text):
    mirrored = mirror(text)
    occ = find_diagonal_dr(word, mirrored)
    return occ

# testing region:
# test = dr_diag_starts(4)
# for d in test:
#     print(d)
# data = read_input('../aoc_data/day04_test.txt')
# test = dr_diag(data, [6, 6])
# print(test)



# action!
data = read_input('../aoc_data/day04.txt')

hor_forw = find_horizontal('XMAS', data)
hor_back = find_horizontal('SAMX', data)
# vertical
ver_forw = find_vertical('XMAS', data)
ver_back = find_vertical('SAMX', data)
# diagonal
# downward, right:
dr_forw = find_diagonal_dr('XMAS', data)
dr_back = find_diagonal_dr('SAMX', data)
# downward, left
dl_forw = find_diagonal_dl('XMAS', data)
dl_back = find_diagonal_dl('SAMX', data)

total = hor_forw + hor_back + ver_forw + ver_back + dr_forw + dr_back + dl_forw + dl_back
print(total)

