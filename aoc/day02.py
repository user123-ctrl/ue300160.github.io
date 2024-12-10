#!/usr/bin/env python

# Red-Nosed Reindeer Nuclear Plant safety reports

from util import read_input

def ascending(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def descending(l):
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            return False
    return True

def monotonic(l):
    return ascending(l) or descending(l)

def within_tolerance(l):
    for i in range(len(l)-1):
        diff = abs(l[i] - l[i+1])
        if not (diff > 0 and diff < 4):
            return False
    return True


def main():
    raw = read_input("../aoc_data/day02.txt")

    # first parse the data to real numbers
    data = [[int(x) for x in line.split()] for line in raw]

    safe_reports = 0
    for report in data:
        if monotonic(report) and within_tolerance(report):
            safe_reports += 1
            # print(report)
        else:
            # loop over all reports that are one level shorter
            for i in range(len(report)):
                shorter = report[:i] + report[i+1:]
                if monotonic(shorter) and within_tolerance(shorter):
                    safe_reports += 1
                    # print(f'safe after removing the {i}th level: {shorter}')
                    break
    print(safe_reports)


if __name__ == '__main__':
    main()