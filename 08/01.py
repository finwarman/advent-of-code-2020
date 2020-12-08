#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('08.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====
visited = set()

insts = []
for i in range(len(rows)):
    op, operand = rows[i].split(' ')
    insts.append((op, int(operand), i))

i = 0
acc = 0
while True:
    current_inst = insts[i]
    op, operand, row = current_inst

    if row in visited:
        print(acc)
        exit()
    visited.add(row)

    if op == "jmp":
        i += operand
    if op == "nop":
        i += 1
    if op == "acc":
        i += 1
        acc += operand
