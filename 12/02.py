#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('12.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

wnorth = 1
weast = 10

north = 0
east = 0

for row in rows:
    op = row[0]
    operand = int(row[1:])

    if op in "LR":
        while operand > 0:
            if op == "L":
                weast, wnorth = -wnorth, weast
            if op == "R":
                weast, wnorth = wnorth, -weast
            operand -= 90
    elif op == "N":
        wnorth += operand
    elif op == "S":
        wnorth -= operand
    elif op == "E":
        weast += operand
    elif op == "W":
        weast -= operand

    elif op == "F":
        east  += weast  * operand
        north += wnorth * operand

    # print(op, operand)
    # print("ship:", north, east)
    # print("wayp:", wnorth, weast)
    # print()

print(abs(north) + abs(east))
