#! /usr/bin/env python3
import re
import math
from copy import deepcopy

# ==== INPUT ====
data = ""
with open('17.txt', 'r') as file:
    data = file.read().strip()

rows = [list(row.strip()) for row in data.split('\n')]

# ==== SOLUTION ====

pad = 5

paddingx = ["." for _ in range(pad)]
padded_rows = [(paddingx + row + paddingx) for row in rows]

paddingy = [["." for _ in range(len(padded_rows[0]))] for _ in range(pad)]
padded_rows = paddingy + padded_rows + paddingy

WIDTH  = len(padded_rows[0])
HEIGHT = len(padded_rows)
DEPTH  = len(padded_rows[0])

MID_DEPTH = DEPTH//2

depth_rows = deepcopy(padded_rows)
for y in range(HEIGHT):
    for x in range(WIDTH):
        depth_rows[y][x] = ['.' for _ in range(DEPTH)]
        depth_rows[y][x][MID_DEPTH] = padded_rows[y][x]

padded_rows = depth_rows

def printGrid(grid, z=MID_DEPTH):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(padded_rows[y][x][z], end = "")
        print()

def countOccupied(s, y, x, z):
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            for dz in range(-1, 2):
                if dy == 0 and dx == 0 and dz == 0:
                    continue

                new_y = y + dy
                new_x = x + dx
                new_z = z + dz

                if  new_y < 0 or new_y >= HEIGHT or \
                    new_x < 0 or new_x >= WIDTH  or \
                    new_z < 0 or new_z >= DEPTH:
                        continue

                if s[new_y][new_x][new_z] == '#':
                    total += 1

    return total

# printGrid(padded_rows)
# print()

d = 0
for i in range(6):
    new = deepcopy(padded_rows)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            for z in range(DEPTH):
                tot = countOccupied(padded_rows, y, x, z)
                cube = padded_rows[y][x][z]

                if cube == '#' and (not(tot == 2 or tot == 3)):
                    new[y][x][z] = '.'
                if cube == '.' and tot == 3: # todo: any z
                    # print(tot, " ", y, x, z)
                    new[y][x][z] = '#'

        # print()
    padded_rows = deepcopy(new)
    # print("Changed:", changes)
    # print("Depth:", d)
    # print()
    # printGrid(padded_rows, MID_DEPTH-d)
    # print()
    # d=+1


tot = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        for z in range(DEPTH):
            if padded_rows[y][x][z] == '#':
                tot += 1
print(tot)
