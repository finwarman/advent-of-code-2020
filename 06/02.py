#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('06.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

tots = {}
tot = 0
groupsize = 0
for row in rows:
    if len(row) < 1:
        for k in tots:
            if tots[k] == groupsize:
                tot += 1
        groupsize = 0
        tots = {}
        continue
    else:
        groupsize += 1
        for c in list(row):
            if c not in tots:
                tots[c] = 0
            tots[c] += 1

print()
print(tot)
