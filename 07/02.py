#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('07.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====
bags = {}

for row in rows:
    colour = row[:row.index(" bags")]
    remains = [col.strip() for col in row[row.index("bags contain ")+13:].replace("bags","").replace("bag", "").replace(".", "").split(",")]

    if remains[0] == "no other":
        continue

    bags[colour] = set()

    for num_col in remains:
        num = int(num_col[:num_col.index(" "):])
        col = num_col[num_col.index(" ")+1:]
        bags[colour].add((col, num))

def dfs(start_colour, dct, count):
    if start_colour not in dct:
        return count
    cols = dct[start_colour]
    for (col, num) in cols:
        count += num * dfs(col, dct, 1)
    return count

print(dfs("shiny gold", bags, 0))
