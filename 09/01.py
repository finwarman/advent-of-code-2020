#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('09.txt', 'r') as file:
    data = file.read().strip()

rows = [int(row.strip()) for row in data.split('\n')]

# ==== SOLUTION ====

preamble = rows[:25]
rows = rows[25:]

for x in rows:
    valid = False
    for p in preamble:
        y = (x-p)
        if (y >= 0) and (y != p) and (y in preamble):
            valid = True
            break

    if not valid:
        print(x)
        quit()

    preamble.append(x)
    preamble = preamble[1:]
