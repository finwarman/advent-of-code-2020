#! /usr/bin/env python3
import re
import math
import numpy as np

# ==== INPUT ====
data = ""
with open('13.txt', 'r') as file:
    data = file.read().strip()

rows = data.split('\n')
buses = []
i = 0
for bus in rows[1].split(","):
    if bus == "x":
        i += 1
        continue
    buses.append((int(bus), i))
    i += 1

print(buses)

# ==== SOLUTION ====

A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X2 = np.linalg.solve(A,B)

print(X2)
