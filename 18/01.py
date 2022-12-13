#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('18.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip().replace('(', '( ').replace(')', ' )').split(' ') for row in data.split('\n')]

# ==== SOLUTION ====

plus  = sum
times = math.prod

def evaluate(statement):
    accumulator = 0
    operator = plus
    while statement:
        element = statement.pop(0)
        if element == '(':
            accumulator = operator((accumulator, evaluate(statement)))
        elif element == ')':
            return accumulator
        elif element == '+':
            operator = plus
        elif element == '*':
            operator = times
        else:
            accumulator = operator((accumulator, int(element)))
    else:
        return accumulator


total = 0
for line in rows:
    ev = evaluate(line)
    # print(ev)
    total += ev

print()
print(total)
