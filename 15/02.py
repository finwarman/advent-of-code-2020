#! /usr/bin/env python3
import re
import math
from collections import defaultdict

# ==== INPUT ====
data = ""
with open('15.txt', 'r') as file:
    data = file.read().strip()

rows = [int(row.strip()) for row in data.split(',')]

# ==== SOLUTION ====
said = defaultdict(int)

rnd = defaultdict(lambda: (0, 0))

last = -1
turn = 0
for num in rows:
    turn += 1

    said[num] += 1
    rnd[num] = (0, turn)
    last = num

    print(num)

print(rnd)

while turn < 30000000:
    turn += 1

    # print(last, said[last], rnd[last], turn)

    num = 0
    if said[last] <= 1:
        num = 0
    else:
        num = rnd[last][1] - rnd[last][0]

    last = num
    said[num] += 1

    t = rnd[num][1]
    rnd[num] = (t, turn)

    # print(num)

print()
print(num)

