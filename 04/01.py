#! /usr/bin/env python3
import re

data = ""
with open('04.txt', 'r') as file:
    data = file.read()

syms = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]
# ignore cid for now

tot = 0
for row in data.strip().split('\n'):


print(tot)
