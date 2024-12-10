#!/usr/bin/env python

# at the toboggan rental shop
from util import read_input
import re

# first, read the raw data
data = read_input("../aoc_data/day03.txt")

# line = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


# res = 0
# for line in data:
#     # find "mul(\d+,\d+)" instances
#     pattern = re.compile('mul\(\d+,\d+\)')
#     matches = pattern.findall(line)
#     for m in matches:
#         tmp = m.split(',')
#         a = int(tmp[0].split('(')[1])
#         b = int(tmp[1][:-1])
#         res += a * b

# print(res)

def run_mul(m):
    tmp = m.split(',')
    a = int(tmp[0].split('(')[1])
    b = int(tmp[1][:-1])
    return a * b

# data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

res = 0
multiply = 1
for i, line in enumerate(data):
    commands = {}
    for m in re.finditer(r'mul\(\d+,\d+\)', line):
        commands[m.start()] = m.group()

    for m in re.finditer(r'do\(\)', line):
        commands[m.start()] = m.group()

    for m in re.finditer(r'don\'t\(\)', line):
        commands[m.start()] = m.group()

    ordered_keys = list(commands.keys())
    ordered_keys.sort()
    
    for k in ordered_keys:
        command = commands[k]
        if command == 'do()':
            multiply = 1
            # print(f'line {i}, pos {k}: {command}')
        elif command == 'don\'t()':
            multiply = 0
            # print(f'line {i}, pos {k}: {command}')
        else:
            res += run_mul(command) * multiply
            # print(f'line {i}, pos {k}: {command}, {multiply}')


print(res)

