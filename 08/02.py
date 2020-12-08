#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('08.txt', 'r') as file:
    data = file.read()

# possibly strip


rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

insts = []
i = -1
for row in rows:
    if not row:
        continue
    i += 1
    op, operand = row.split(' ')
    insts.append([op, int(operand), i])


last = len(insts) - 1

def runProg(linesin):
    visited = set()
    i = 0
    acc = 0
    while True:
        current_inst = linesin[i]
        op, operand, row = current_inst

        if row in visited:
            return
        visited.add(row)

        if op == "jmp":
            i += operand
        elif op == "nop":
            i += 1
        elif op == "acc":
            i += 1
            acc += operand

        if i > last:
            print("Result:", acc)
            return

for i in range(len(insts)):
    newinsts = insts.copy()

    op, operands, line = newinsts[i]
    if op == "nop":
        newinsts[i] = ["jmp", operands, line]
    elif op == "jmp":
        newinsts[i] = ["nop", operands, line]
    else:
        continue

    runProg(newinsts)
