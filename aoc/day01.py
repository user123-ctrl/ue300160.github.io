#!/usr/bin/env python

# chief historian's office; comparing reports
from util import read_input

test = "The quick brown foxdid not jump over the lazy dog.Instead, it pounced."

# a function that counts occurrences of x in list l
def count_occurrences(x, l):
    counter = 0
    for number in l:
        if x == number:
            counter += 1
    return counter

# first, read the raw data
raw = read_input("../aoc_data/day01_test.txt")
list_a = []
list_b = []
for line in raw:
    tmp = line.split(' ')
    a = int(tmp[0])
    b = int(tmp[-1])
    list_a.append(a)
    list_b.append(b)

# print(list_a)
# print(list_b)

# now we need to sort the lists
list_a.sort()
list_b.sort()
# print(list_a)

# calculate differences!
sum_of_differences = 0
for a, b in zip(list_a, list_b):
    diff = abs(a - b)
    sum_of_differences += diff

# print(sum_of_differences)
# Solve the second part:

print(count_occurrences(3, list_b))
print(count_occurrences(4, list_b))
print(count_occurrences(23, list_b))
