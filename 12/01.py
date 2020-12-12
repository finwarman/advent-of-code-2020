#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('12.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====
total = 0

north = 0
east = 0
d = 90

for row in rows:
    op = row[0]
    operand = int(row[1:])

    if op == "R":
        d = (d + operand) % 360
    if op == "L":
        d = (d - operand) % 360
    elif op == "N":
        north += operand
    elif op == "S":
        north -= operand
    elif op == "E":
        east += operand
    elif op == "W":
        east -= operand
    elif op == "F":
        if   d == 0:
            north += operand
        elif d == 90:
            east += operand
        elif d == 180:
            north -= operand
        elif d == 270:
            east -= operand

    print(op, operand, ":", east, north, "dir:", d)

print()
print(abs(north) + abs(east))

