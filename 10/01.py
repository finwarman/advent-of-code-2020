#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('10.txt', 'r') as file:
    data = file.read().strip()

rows = sorted([int(row.strip()) for row in data.split('\n')])

# ==== SOLUTION ====

def getJoltageChain(currentJoltage, jolts, chain):
    if len(jolts) == 1:
        print("Done!")
        chain.append((jolts[0], jolts[0] - currentJoltage))
        return chain
    for i in range(len(jolts)):
        jolt = jolts[i]
        d = jolt - currentJoltage
        if d > 0 and d <= 3:
            chain.append((jolt, d))
            return getJoltageChain(jolt, jolts[i+1:], chain)


chain = getJoltageChain(0, rows, [])

ones = 0
threes = 1 # for final connection
for r in chain:
    if r[1] == 1:
        ones += 1
    if r[1] == 3:
        threes += 1

print(ones, threes)
print(ones * (threes))
