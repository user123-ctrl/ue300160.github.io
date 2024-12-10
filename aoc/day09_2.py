#!/usr/bin/env python

# Windows Disk Manager
from util import read_input
from tqdm import tqdm

# fs = '2333133121414131402'
fs = read_input('../aoc_data/day09.txt')[0]

# go over the memory blocks and write them out
def unzip(fs):
    disk = ''
    for i, m in enumerate(fs):
        if i % 2 == 0: # this is a file
            # the file string is the index divided by 2, printed m times
            disk += str(i//2) * int(m)
        else: # this is a free memory block
            # the free memory string is the '.' char printed m times
            disk += '.' * int(m)
    return disk

def find_blocks(disk):
    blocks = []
    prev = ''
    block = ''
    for c in disk + 'X':
        if c == prev:
            block += c
        else:
            blocks.append(block)
            prev = c
            block = c

    return [b for b in blocks if b != '']

def move_file(f, blocks):
    for i, b in enumerate(blocks):
        # print(f'moving file {f}; checking block {b}')
        if f[0] in b:
            break
        if '.' not in b:
            continue
        if len(f) <= len(b):
            new_block = f + b[len(f):]
            new_disk = ''.join(blocks[:i]) + new_block + ''.join(blocks[(i+1):]).replace(f[0], '.')
            return new_disk
    return ''.join(blocks)

def defragment(disk):
    # print(files[::-1])
    blocks = find_blocks(disk)
    files = [b for b in blocks if '.' not in b]
    for f in tqdm(files[::-1]):
        # print(disk)
        # print(blocks)
        disk = move_file(f, blocks)
        blocks = find_blocks(disk)
    return disk

def checksum(disk):
    res = 0
    for i, block in enumerate(disk):
        if block == '.':
            continue
        else:
            res += i * int(block)
    return res

disk = unzip(fs)
defrag = defragment(disk)
print(checksum(defrag))