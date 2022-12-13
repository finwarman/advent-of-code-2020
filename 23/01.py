#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('23.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')]
cups = [int(x) for x in list(rows[0])]

# ==== SOLUTION ====

l = len(cups)
for i in range(0, 100):
    current_cup = cups[i % l]

    x, y, z = cups[(i+1) % l], cups[(i+2) % l], cups[(i+3) % l]
    for c in (x,y,z):
        del cups[cups.index(c)]

    dest_label = current_cup - 1
    while dest_label not in cups:
        dest_label -= 1
        if dest_label < 1:
            dest_label = 9
    dest_index = cups.index(dest_label)

    cups = cups[:dest_index+1] + [x, y, z] + cups[dest_index+1:]

    while cups[i % l] != current_cup:
        cups = cups[1:] + [cups[0]]


split = cups.index(1)
print(''.join([str(x) for x in cups[split+1:] + cups[:split]]))
