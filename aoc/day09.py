#!/usr/bin/env python

# Windows Disk Manager
from util import read_input
import copy
from tqdm import tqdm

# fs = '2333133121414131402'
fs = read_input('../aoc_data/day09.txt')[0]

# go over the memory blocks and write them out
def unzip(fs):
    disk = []
    for i, m in enumerate(fs):
        if i % 2 == 0: # this is a file
            # the file string is the index divided by 2, printed m times
            disk += [str(i//2)] * int(m)
        else: # this is a free memory block
            # the free memory string is the '.' char printed m times
            disk += ['.'] * int(m)
    return disk

# a function that moves the last file block into the current empty block
def shuffle(disk):
    reshuffled = copy.deepcopy(disk)
    to_move = -1
    for i, block in enumerate(reshuffled):
        if block == reshuffled[to_move]:
            break
        elif block == ".":
            val = disk[to_move]
            reshuffled[i] = val
            reshuffled[to_move] = '.'
            to_move -= 1
            while disk[to_move] == '.':
                to_move -= 1

    return reshuffled

def checksum(disk):
    res = 0
    for i, block in enumerate(disk):
        if block == '.':
            return res
        else:
            res += i * int(block)

disk = unzip(fs)
reshuffled = shuffle(disk)
print(checksum(reshuffled))