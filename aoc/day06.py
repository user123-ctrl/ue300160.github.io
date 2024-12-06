#!/usr/bin/env python

# solid snake
from util import read_input
import time

facility_map = read_input('../aoc_data/day06.txt')

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

def marauders_map(x, y, direction, actual_map):
    for i, line in enumerate(actual_map):
        if x != i:
            print(line)
        else:
            newline = line[:y] + direction + line[(y+1):]
            print(newline)

# def update_map(x, y, actual_map, marker='X'):
#     for i, line in enumerate(actual_map):
#         if x != i:
#             continue
#         else:
#             newline = line[:y] + marker + line[(y+1):]
#             actual_map[x] = newline
#             break

# print(out_of_bounds(0, 5, facility_map)) # should be False
# print(out_of_bounds(-1, 5, facility_map)) # should be True
# print(out_of_bounds(1, -5, facility_map)) # should be True
# print(out_of_bounds(11, 5, facility_map)) # should be True
# print(out_of_bounds(1, 13, facility_map)) # should be True

start_x, start_y, direction = find_guard(facility_map)
print(start_x, start_y, direction)
# replace the starting position with a dot!
to_replace = facility_map[start_x]
new_line = to_replace[:start_y] + '.' + to_replace[(start_y+1):]
facility_map[start_x] = new_line

# let the guard walk
positions_visited = []
x_now, y_now = start_x, start_y
positions_visited.append([x_now, y_now])
for i in range(6000):
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
    if [x_now, y_now] not in positions_visited:
        positions_visited.append([x_now, y_now])
    # marauders_map(x_now, y_now, direction, facility_map)
    # # # update_map(x_now, y_now, facility_map, marker='X')
    # print('=======================')
    # time.sleep(0.05)

# conditions for leaving the map:
# x < 0 or x > N_x
# y < 0 or y > N_y
    
print(len(positions_visited))

# print(x_now, y_now)
