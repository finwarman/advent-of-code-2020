#! /usr/bin/env python3
import re

data = ""
with open('02.txt', 'r') as file:
    data = file.read()

tot = 0
for row in data.strip().split('\n'):
    p = re.compile("(\d+)-(\d+) ([a-z]): (.*)")
    match = p.match(row.strip())

    x = int(match.group(1))
    y = int(match.group(2))
    char = match.group(3)
    string = match.group(4)

    if (string[x-1] == char) ^ (string[y-1] == char):
        tot += 1

print(tot)


