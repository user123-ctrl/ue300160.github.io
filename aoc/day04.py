#!/usr/bin/env python

# elf crossword puzzles
from util import read_input

# first, read the raw data
data = read_input("../aoc_data/day04.txt")

# horizontal, vertical, diagonal
# forwards, backwards

def count_occ(word, text):
    res = 0
    for line in text:
        res += line.count(word)
    return res

def transpose(text):
    columns = [''] * len(text[0])
    for i, line in enumerate(text):
        for j, letter in enumerate(line):
            columns[j] += letter
    return columns

def diag_starts_down(n):
    starts = []
    for i in range(n):
        starts.append([0, i])
        starts.append([i, 0])
    return starts

def diag_starts_up(n):
    starts = []
    for i in range(n):
        starts.append([n-1, i])
        starts.append([i, 0])
    return starts

def diagonify_down(text):
    diagonals = []
    n = len(text)
    starts = diag_starts_down(n)
    for start in starts:
        i, j = start
        diag_ij = ""
        while i < n and j < n:
            diag_ij += text[i][j]
            i += 1
            j += 1
        diagonals.append(diag_ij)
    return diagonals

def diagonify_up(text):
    diagonals = []
    n = len(text)
    starts = diag_starts_up(n)
    for start in starts:
        i, j = start
        diag_ij = ""
        while j < n and i > -1:
            diag_ij += text[i][j]
            i -= 1
            j += 1
        diagonals.append(diag_ij)
    return diagonals

total_xmas = 0

# test = [
#     '12345',
#     '67890',
#     'abcde',
#     'fghij',
#     'klmno'
# ]

# print(diagonify_up(test))


# first horizontal, which is the easiest
horizontal_forward = count_occ('XMAS', data)
horizontal_backward = count_occ('SAMX', data)
# now the same for the transposed text
transposed = transpose(data)
vertical_forward = count_occ('XMAS', transposed)
vertical_backward = count_occ('SAMX', transposed)
# now all the diagonals
diagonals = set(diagonify_down(data))
diag_down_forward = count_occ('XMAS', diagonals)
diag_down_backward = count_occ('SAMX', diagonals)
diagonals = set(diagonify_up(data))
diag_up_forward = count_occ('XMAS', diagonals)
diag_up_backward = count_occ('SAMX', diagonals)

total = horizontal_forward + horizontal_backward + vertical_forward + vertical_backward + diag_down_forward + diag_down_backward + diag_up_forward + diag_up_backward
# print(total)

# part 2: all of this was for nothing, now please find crossing MAS instead

def xmas(text, i, j):
    # given that there is an A at position i, j
    # can we find an X-MAS around it?
    diag_a = text[i-1][j-1] + text[i][j] + text[i+1][j+1]
    diag_b = text[i-1][j+1] + text[i][j] + text[i+1][j-1]

    diag_a_mas = diag_a == 'MAS' or diag_a == 'SAM'
    diag_b_mas = diag_b == 'MAS' or diag_b == 'SAM'
    if diag_a_mas and diag_b_mas:
        return True
    return False

total_xmas = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data)-1):
        if data[i][j] == 'A':
            total_xmas += xmas(data, i, j)

print(total_xmas)