#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('09.txt', 'r') as file:
    data = file.read().strip()

rows = [int(row.strip()) for row in data.split('\n')]

# ==== SOLUTION ====

target_sum = 1398413738

tot = rows[0]
i = 0
j = 1
while j <= len(rows):

    while((tot > target_sum) and (i < j)):
        tot = tot - rows[i]
        i += 1

    if tot == target_sum:
        print("\nFound!")
        win = rows[i:j]
        print(sum(win))
        print(min(win), max(win))
        print("\nOutput:")
        print(sum([min(win), max(win)]))
        print()
        quit()

    if (j < len(rows)):
        tot = tot + rows[j]

    j += 1
