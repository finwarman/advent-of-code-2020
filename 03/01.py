#! /usr/bin/env python3
import re

x, y = (0, 0)

data = ""
with open('03.txt', 'r') as file:
    data = file.read()

data = data.strip().split('\n')

width = len(data[0].strip())
height = len(data)

tot = 0
while y < height:
    if data[y][x%width] == '#':
        tot+=1
    x += 3
    y += 1

print(tot)
