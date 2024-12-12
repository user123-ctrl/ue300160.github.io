#!/usr/bin/env python

# hiking in the lava fields
from util import read_input
import copy

def to_integer(topomap):
    n = len(topomap)
    newmap = []
    for i, row in enumerate(topomap):
        newmap.append([])
        for j, tile in enumerate(row):
            if tile == '.':
                tile = 12
            newmap[i].append(int(tile))
    return newmap

def find_trail_spots(grid, spot=0):
    starts = []
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if grid[i][j] == spot:
                starts.append([i, j])
    return starts

def north(loc):
    i, j = loc
    return i-1, j

def south(loc):
    i, j = loc
    return i+1, j

def east(loc):
    i, j = loc
    return i, j+1

def west(loc):
    i, j = loc
    return i, j-1

def within_bounds(loc, grid):
    n = len(grid)
    i, j = loc
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    return True

def on_trail(current, next, grid):
    i, j = current
    ii, jj = next
    if grid[ii][jj] - grid[i][j] == 1:
        return True
    return False

def arrived(loc, grid, val=9):
    i, j = loc
    if grid[i][j] == val:
        return True
    return False

def follow_trail(grid, start, found):
    if arrived(start, grid) and start not in found:
        found.append(start)
        return 1

    directions = [north, south, east, west]
    result = 0
    for d in directions:
        next_step = d(start)
        if within_bounds(next_step, grid) and on_trail(start, next_step, grid):
            # print(f'going from {start}: {grid[start[0]][start[1]]} to {next_step}: {grid[next_step[0]][next_step[1]]}')
            # result += follow_trail(grid, next_step, found) # this is for part 1
            result += follow_trail(grid, next_step, []) # part 2
    return result

def main():
    topomap = read_input('../aoc_data/day10.txt')
    grid = to_integer(topomap)
    starts = find_trail_spots(grid)
    trail_score = 0
    for s in starts:
        trail_score += follow_trail(grid, s, [])
        exit
    print(trail_score)


if __name__ == '__main__':
    main()