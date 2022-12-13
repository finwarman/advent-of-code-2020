#! /usr/bin/env python3

import re
import math
import collections

# ==== INPUT ====
data = ""
with open('14.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def mask_bits(mask, number):
    x = number
    for i in range(35, -1, -1):
        if mask[i] == "1":
            number = set_bit(number, 35-i)
        elif mask[i] == "0":
            number = clear_bit(number, 35-i)
    return number

memory = {}
mask = "X" * 36

for row in rows:
    s = row.split(" ")
    if s[0] == "mask":
        mask = s[2]
    else:
        address = int(s[0][4:-1])
        val = int(s[2])
        val = mask_bits(mask, val)
        memory[address] = val

print()
print(sum(memory.values()))
print()
