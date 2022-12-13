#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('16.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====
limits = []

rowslim = 20
# rowslim = 3

otherslim = 25
# otherslim = 8

for row in rows[:rowslim]:
    row = row[row.find(': ')+2:]
    split = row.split(" ")

    la1, la2 = split[0].split("-")
    limits.append(  (int(la1), int(la2))  )

    lb1, lb2 = split[2].split("-")
    limits.append(  (int(lb1), int(lb2))  )

tot = 0
# other tickets

for row in rows[otherslim:]:
    for val in row.split(","):
        # print(val, end=" ")
        val = int(val)
        valid = False
        for pair in limits:
            if (pair[0] <= val <= pair[1]):
                valid = True
                break

        if not valid:
            # print("(INVALID) ", end="")
            tot += val

        # print(",", end=" ")
    # print()


print(tot)
