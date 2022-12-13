#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('13.txt', 'r') as file:
    data = file.read().strip()

rows = data.split('\n')
target_time = int(rows[0].strip())
buses = [int(bus) for bus in rows[1].split(",") if bus != "x"]

print(buses)

print(target_time)
print()

# ==== SOLUTION ====
earliest = math.inf
early_id = 1

for bus in buses:
    x = bus
    while x < target_time:
        x += bus
    diff = x - target_time
    print(bus, x, diff)
    if diff < earliest:
        early_id = bus
        earliest = diff

print()
print(early_id, earliest, early_id * earliest)
