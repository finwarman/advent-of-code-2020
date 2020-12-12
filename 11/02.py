#! /usr/bin/env python3
import re
import math
from copy import copy, deepcopy

# ==== INPUT ====
data = ""
with open('11.txt', 'r') as file:
    data = file.read().strip()

rows = [list(row.strip()) for row in data.split('\n')]

# ==== SOLUTION ====
WIDTH  = len(rows[0])
HEIGHT = len(rows)

NEIGHBOUR_OFFSETS = [(x,y) for x in range(-1, 2) for y in range(-1, 2) if x|y != 0]
# [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def countOccupied(s, y, x):
    total = 0
    for dy, dx in NEIGHBOUR_OFFSETS:
        new_y = y + dy
        new_x = x + dx
        ch = ""
        while ch != "L" and ch != "#" and new_y >= 0 and new_y < HEIGHT and new_x >= 0 and new_x < WIDTH:
            ch = s[new_y][new_x]
            new_y += dy
            new_x += dx
        if ch == "#":
            total += 1
    return total

t = rows
changed = 1
while changed > 0:
    new_s = deepcopy(rows)
    changed = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            s = rows[y][x]
            if s == ".":
                continue
            c = countOccupied(rows, y, x)
            if c == 0 and s == "L":
                new_s[y][x] = "#"
                changed += 1
            elif c >= 5 and s == "#":
                new_s[y][x] = "L"
                changed += 1

    t = rows
    rows = deepcopy(new_s)

print("".join(sum(rows, [])).count('#'))

# === Helpers:

# def printstate(seats):
#     print()
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(seats[y][x], end="")
#         print()
#     print()
