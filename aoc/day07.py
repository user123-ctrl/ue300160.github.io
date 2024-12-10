#!/usr/bin/env python

# solid snake
from util import read_input
from tqdm import tqdm

equations = read_input('../aoc_data/day07.txt')

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def combine(x, y):
    s = str(x) + str(y)
    return int(s)

def evaluate(numbers, operators, result):
    tmp = numbers[0]
    for i, opp in enumerate(operators):
        tmp = opp(tmp, numbers[i+1])
    
    # print(tmp)
    if tmp == result:
        return True, tmp
    return False, tmp

def permute(opps, n):
    base = len(opps)
    permutations = [[] for i in range(base**n)]

    for j in range(base**n):
        for i in range(n):
            loc = (j // base**i) % base
            permutations[j].append(opps[loc])
    return permutations


calibration = 0
for line in tqdm(equations):
    # print(line)
    s, num = line.split(':')
    result = int(s)
    numbers = [int(x) for x in num.strip().split()]
    permutations = permute([add, multiply, combine], len(numbers)-1)
    # print(result, numbers)
    # for p in permutations:
        # print(p)
    for perm in permutations:
        works, calc = evaluate(numbers, perm, result)
        if works:
            calibration += calc
            break

print(calibration)