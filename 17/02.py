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

def get_neighbours(y, x, z, w):
    n = set()
    for y1 in range(-1, 2):
        for x1 in range(-1, 2):
            for z1 in range(-1, 2):
                for w1 in range(-1, 2):
                    if y1 != 0 or x1 != 0 or z1 != 0 or w1 != 0:
                        n.add((y1 + y, x1 + x, z1 + z, w1 + w))
    return n

WIDTH = len(rows)
HEIGHT = len(rows[0])

active = set()
for y in range(WIDTH):
    for x in range(HEIGHT):
        if rows[y][x] == "#":
            active.add((y, x, 0, 0))

for i in range(6):
    new_active = deepcopy(active)
    checked = set()

    for cube in active:
        checked.add(cube)
        neighbours = get_neighbours(*cube)

        active_neighbours = [n for n in neighbours if n in active]
        active_neighbour_count = len(active_neighbours)

        if active_neighbour_count != 2 and active_neighbour_count != 3:
            new_active.remove(cube)

        for neigh in neighbours:
            if neigh not in active_neighbours and neigh not in checked:
                checked.add(neigh)

                curr_neighbours = get_neighbours(*neigh)
                curr_active_count = 0
                for cn in curr_neighbours:
                    if cn in active:
                        curr_active_count += 1

                if curr_active_count == 3:
                    new_active.add(neigh)


    active = new_active

print(len(active))
