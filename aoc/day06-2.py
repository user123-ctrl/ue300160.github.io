#!/usr/bin/env python

# solid snake
from util import read_input
import time
import curses
from curses import wrapper

facility_map = read_input('../aoc_data/day06_test.txt')

# print(facility_map)

def north(i, j):
    return i-1, j

def south(i, j):
    return i+1, j

def east(i, j):
    return i, j+1

def west(i, j):
    return i, j-1

directions = ['>', '<', '^', 'v']
turns = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

def find_guard(minimap, directions=directions):
    for i, line in enumerate(minimap):
        for j, position in enumerate(line):
            if position in directions:
                return i, j, position
    return None

def try_walking(x, y, direction):
    if direction == '^':
        return north(x, y)
    elif direction == '>':
        return east(x, y)
    elif direction == '<':
        return west(x, y)
    elif direction == 'v':
        return south(x, y)
    else:
        return None

def out_of_bounds(x, y, some_map):
    # returns True when the position is outside the map's coordinates
    too_far_north = x < 0
    too_far_south = x > len(some_map) - 1
    too_far_west = y < 0
    too_far_east = y > len(some_map[0]) - 1
    is_out = too_far_west or too_far_east or too_far_north or too_far_south
    return is_out

def marauders_map(x, y, direction, actual_map, screen):
    screen.clear()
    for i, line in enumerate(actual_map):
        if x != i:
            screen.addstr(line + '\n')
        else:
            newline = line[:y] + direction + line[(y+1):]
            screen.addstr(newline + '\n')
    

def update_map(x, y, actual_map, marker='X'):
    updated_map = []
    for i, line in enumerate(actual_map):
        if x != i:
            updated_map.append(line)
        else:
            newline = line[:y] + marker + line[(y+1):]
            updated_map.append(newline)
    return updated_map


def modified_walk(facility_map, obstacle):
    obstacled_map = update_map(obstacle[0], obstacle[1], facility_map, marker='O')
    return loops(obstacled_map)
    

def trace_steps(facility_map, verbose=True):
    start_x, start_y, direction = find_guard(facility_map)
    # replace the starting position with a dot!
    to_replace = facility_map[start_x]
    new_line = to_replace[:start_y] + '.' + to_replace[(start_y+1):]
    facility_map[start_x] = new_line
    # print the map once first so that we can see what's happening
    if verbose:
        screen = curses.initscr()
        marauders_map(start_x, start_y, direction, facility_map, screen)
        screen.refresh()
        curses.napms(100)
        screen.clear()
        time.sleep(1)

    steps = []
    x_now, y_now = start_x, start_y
    steps.append([x_now, y_now, direction])
    while not out_of_bounds(x_now, y_now, facility_map):
        # imagine the guard was taking a step
        x_try, y_try = try_walking(x_now, y_now, direction)
        # does this step take him out of the map?
        if out_of_bounds(x_try, y_try, facility_map):
            break
        # is he trying to walk on a normal tile...
        if facility_map[x_try][y_try] == '.':
            x_now, y_now = x_try, y_try
        # ...or is he finding an obstacle?
        else: # make a 90° right turn
            direction = turns[direction]
            x_now, y_now = try_walking(x_now, y_now, direction)
        if [x_now, y_now, direction] not in steps:
            steps.append([x_now, y_now, direction])
        else:
            print("found loop!")

        if verbose:
            marauders_map(x_now, y_now, direction, facility_map, screen)
            screen.refresh()
            curses.napms(100)
    if verbose:
        curses.endwin()
    return steps

def loops(facility_map):
    start_x, start_y, direction = find_guard(facility_map)
    # replace the starting position with a dot!
    to_replace = facility_map[start_x]
    new_line = to_replace[:start_y] + '.' + to_replace[(start_y+1):]
    facility_map[start_x] = new_line

    steps = []
    x_now, y_now = start_x, start_y
    steps.append([x_now, y_now, direction])
    while not out_of_bounds(x_now, y_now, facility_map):
        # imagine the guard was taking a step
        x_try, y_try = try_walking(x_now, y_now, direction)
        # does this step take him out of the map?
        if out_of_bounds(x_try, y_try, facility_map):
            break
        # is he trying to walk on a normal tile...
        if facility_map[x_try][y_try] == '.':
            x_now, y_now = x_try, y_try
        # ...or is he finding an obstacle?
        else: # make a 90° right turn
            direction = turns[direction]
            x_now, y_now = try_walking(x_now, y_now, direction)
        if [x_now, y_now, direction] not in steps:
            steps.append([x_now, y_now, direction])
        else:
            return True
    return False

steps = trace_steps(facility_map, verbose=False)
# print(steps)
# print(modified_walk(facility_map, obstacle=[6, 3]))
print(loops(facility_map))