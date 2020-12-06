#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('06.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

tots = set()
tot = 0
for row in rows:
    if len(row) < 1:
        tot += len(tots)
        tots = set()
        continue
    else:
        for c in list(row):
            tots.add(c)

print(tot)
