#!/usr/bin/env python

# tinfoil time
from util import read_input

def find_antennae(grid):
    antennae = {}
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == '.': # keep reading, not interesting
                continue
            else:
                if c not in antennae.keys():
                    antennae[c] = []
                antennae[c].append([i, j])
    return antennae

def inside_map(spot, n):
    i, j = spot
    if i < 0 or i > n-1 or j < 0 or j > n-1:
        return False
    return True

def find_antinodes(t1, t2, n):
    di = t1[0] - t2[0]
    dj = t1[1] - t2[1]
    a1 = [t2[0] + di*2, t2[1] + 2*dj]
    a2 = [t2[0] - di, t2[1] - dj]
    result = []
    # one direction:
    if inside_map(a1, n):
        result.append(a1)
    if inside_map(a2, n):
        result.append(a2)
    return result

# testing
grid = read_input('../aoc_data/day08.txt')
antennae = find_antennae(grid)
n = len(grid)
# print(n)
antinodes = list()
for freq in antennae:
    for i, t1 in enumerate(antennae[freq]):
        for j, t2 in enumerate(antennae[freq][i+1:]):
            potential = find_antinodes(t1, t2, n)
            for pot_antinode in potential:
                # print(f'node1: {t1}, node2: {t2}, antinode1: {pot_antinode}')
                if pot_antinode not in antinodes:
                    antinodes.append(pot_antinode)

# print(antinodes)
print(len(antinodes))