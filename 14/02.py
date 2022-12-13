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

def generate_masks(mask, index, results):
    if index < 0:
        return results
    else:
        new_res = []
        if mask[index] == "X":
            for m in results:
                new_res.append("0" + m)
                new_res.append("1" + m)
        else:
            for m in results:
                new_res.append(("-" if mask[index]=="0" else "1") + m)
        return generate_masks(mask, index-1, new_res)


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
masks = None

for row in rows:
    s = row.split(" ")
    if s[0] == "mask":
        mask = s[2]
        masks = None
    else:
        address = int(s[0][4:-1])
        val = int(s[2])
        if not masks:
            masks = generate_masks(mask, 35, [""])
        addresses = []
        for m in masks:
            addr = mask_bits(m, address)
            memory[addr] = val


print()
print(sum(memory.values()))
print()
