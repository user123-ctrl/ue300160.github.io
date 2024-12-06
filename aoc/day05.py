#!/usr/bin/env python

# printing manuals
from util import read_input

# first, read the raw data
data = read_input("../aoc_data/day05.txt")

page_ordering = []
updates = []
for line in data:
    if "|" in line:
        page_ordering.append([int(x) for x in line.split("|")])
    if "," in line:
        updates.append([int(x) for x in line.split(",")])

# print(page_ordering)
# print(updates)

def is_valid(update, page_ordering):
    for i, x in enumerate(update):
        for y in update[(i+1):]:
            if [x, y] not in page_ordering:
                return False
    return True

def fix_invalid(update, page_ordering):
    # calculate how many connections there
    # are between x,y in the page ordering rules
    primacy = {}
    for x in update:
        primacy[x] = calc_primacy(x, update, page_ordering)
    # the number with the highest primacy must be
    # the one on the beginning of the row
    fixed = sort_dict_by_value(primacy)
    return fixed

def sort_dict_by_value(dictionary):
    # the sort() method sorts the keys of a dictionary
    # so if we reverse the key/value pairs we can easily get it:
    reverse_dict = {v: k for k, v in dictionary.items()}
    keys = list(reverse_dict.keys())
    keys.sort(reverse=True)
    sorted_values = [reverse_dict[k] for k in keys]
    return sorted_values

def calc_primacy(x, update, page_ordering):
    primacy = 0
    for y in update:
        if [x, y] in page_ordering:
            primacy += 1
    return primacy

# print(is_valid(updates[0], page_ordering))
result = 0
for update in updates:
    if is_valid(update, page_ordering):
        n = len(update)
        # result += update[n//2]
    else:
        fixed = fix_invalid(update, page_ordering)
        n = len(update)
        result += fixed[n//2]

print(result)