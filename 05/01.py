#! /usr/bin/env python3
import re

data = ""
with open('05.txt', 'r') as file:
    data = file.read().strip()

# ignore cid for now
import math
maxseat = -1
for row in data.strip().split('\n'):
    bins = row[0:7]
    lr   = row[7:]
    rng = (0, 127)
    for binc in bins[0:-1]:
        diff = int(rng[1]) - int(rng[0]) + 1
        half = diff // 2
        print(rng)
        if binc == "F":
            # lower half
            rng = (rng[0], rng[1] - half)
        else:
            # upperhalf
            rng = (rng[0] + half, rng[1])

    print(rng)
    print(row, bins, lr)
    seatrow = int(rng[0]) if bins[-1]=="F" else (int(rng[1]))

    rng = (0, 7)
    for stc in lr[0:-1]:
        diff = int(rng[1]) - int(rng[0]) + 1
        half = diff // 2

        if stc == "L":
            # lower half
            rng = (rng[0], rng[1] - half)
        else:
            # upperhalf
            rng = (rng[0] + half, rng[1])

    seatno = int(rng[0]) if lr[-1]=="L" else (int(rng[1]))

    sid = seatrow * 8 + seatno
    print(rng)
    print(seatrow, seatno, sid)
    maxseat = max(maxseat, sid)

    print()

print(maxseat)
