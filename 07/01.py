#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('07.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')]

bags = {}

# ==== SOLUTION ====
total = 0

for row in rows:
    if not row:
        continue
    colour = row[:row.index(" bags")]
    remains = [col.strip() for col in row[row.index("bags contain ")+13:].replace("bags","").replace("bag", "").replace(".", "").split(",")]

    if remains[0] == "no other":
        continue

    bags[colour] = set()

    for num_col in remains:
        col = num_col[num_col.index(" ")+1:]
        bags[colour].add(col)


def dfs(start_colour, dict):
    if start_colour not in dict:
        return False
    cols = dict[start_colour]
    for col in cols:
        if col == "shiny gold":
            return True
        else:
             if dfs(col, dict):
                 return True
    return False

for colour in bags.keys():
    if dfs(colour, bags):
        total += 1

print(total)
