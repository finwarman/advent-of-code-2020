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
print(HEIGHT, WIDTH)

def countOccupied(s, y, x):
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            new_y = y + dy
            new_x = x + dx

            if new_y < 0 or new_y >= HEIGHT or \
                new_x < 0 or new_x >= WIDTH:
                    continue

            if s[new_y][new_x] == "#":
                # print(s[new_y][new_x])
                total += 1

    return total

def printstate(seats):
    print()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(seats[y][x], end="")
        print()
    print()

# printstate(rows)


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
            elif c >= 4 and s == "#":
                new_s[y][x] = "L"
                changed += 1

    t = rows
    rows = deepcopy(new_s)

print("".join(sum(rows, [])).count('#'))
