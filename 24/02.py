#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('24.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

directions = {"e":(1,0), "w":(-1,0), "ne":(1,-1),  "nw":(0,-1), "se":(0,1), "sw":(-1,1)}

grid = {}

def addNeighborsToGrid(tileCoords: tuple):
  q, r  = tileCoords
  for dirs in directions.values():
    dq, dr = dirs
    neighbor =  (q + dq, r + dr)
    if not neighbor in grid:
      grid[neighbor] = 'w'

for line in rows:
    steps = []
    q, r = 0, 0
    i = 0
    while i < len(line):
      ch = line[i]
      if ch == 'n' or ch == 's':
        steps.append(f'{ch}{line[i+1]}')
        i += 1
      else:
        steps.append(ch)
      i += 1

    for step in steps:
      hDir = directions[step]
      q += hDir[0]
      r += hDir[1]

    if (q, r) in grid and grid[(q, r)] == 'b':
      grid[(q, r)] = 'w'
    else:
      grid[(q, r)] = 'b'

    addNeighborsToGrid((q, r))

for i in range(100):
  tilesToFlip = dict()
  for (q, r), color in grid.items():
    numBlack = 0
    for dirs in directions.values():
      dq, dr = dirs
      neighbor =  (q + dq, r + dr)
      if neighbor in grid and grid[neighbor] == 'b':
          numBlack += 1
    if color == 'b' and (numBlack == 0 or numBlack > 2):
      tilesToFlip[(q, r)] = 'w'
    elif color == 'w' and numBlack == 2:
      tilesToFlip[(q, r)] = 'b'

  for (q, r), color in tilesToFlip.items():
    grid[(q, r)] = color
    addNeighborsToGrid((q, r))

print(f"\nPart 2\n{len([t for t in grid.values() if t == 'b'])}")
