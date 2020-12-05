#! /usr/bin/env python3
import re


slopes = [
    [(0,0), (1, 1)],
    [(0,0), (3, 1)],
    [(0,0), (5, 1)],
    [(0,0), (7, 1)],
    [(0,0), (1, 2)]
]

data = ""
with open('03.txt', 'r') as file:
    data = file.read()

data = data.strip().split('\n')

width = len(data[0].strip())
height = len(data)

totm = 1

for slope in slopes:
    tot = 0
    x, y = slope[0]
    xdel, ydel = slope[1]
    while y < height:
        if data[y][x%width] == '#':
            tot+=1
        x += xdel
        y += ydel
    totm = tot * totm

print(totm)
