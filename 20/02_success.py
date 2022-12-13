#! /usr/bin/env python3
import re
import math
from collections import defaultdict
import numpy as np
from scipy import signal
from copy import deepcopy

# ==== INPUT ====
lines = ""
with open('20.txt', 'r') as file:
# with open('test_20.txt', 'r') as file:
    lines = file.read().strip()

data = lines.split('\n')
tiles_list = [[row.strip() for row in tile.split('\n')] for tile in lines.split('\n\n')]

# ==== SOLUTION ====

tiles = {}

for tile in tiles_list:
    uid = int(''.join(tile[0][5:-1]))
    pixels = tile[1:]

    new = []
    for line in pixels:
        curr = []
        for px in line:
            curr.append(0 if px == "." else 1)
        new.append(curr)
    tiles[uid] = np.array(new)


tile_edges = {}

generated_tilesets = {}
def getAllOrientations(uid, tile):
    if uid in generated_tilesets:
        return generated_tilesets[uid]

    tiles = []
    tiles.append(tile)

    tiles.append(np.rot90(tile, 1))
    tiles.append(np.rot90(tile, 2))
    tiles.append(np.rot90(tile, 3))

    tiles.append(np.flipud(tile))
    tiles.append(np.flip(tile))

    tiles.append(np.rot90(np.flipud(tile), 1))
    tiles.append(np.rot90(np.flipud(tile), 2))
    tiles.append(np.rot90(np.flipud(tile), 3))
    generated_tilesets[uid] = tiles
    return tiles

dim = math.isqrt(len(tiles)+1)
grid = [[{} for x in range(dim)] for y in range(dim)]

print("building grid...")

def buildgrid(x, y, cubelen, grid, tiles):
    if len(tiles) == 0:
        return grid

    for uid, tile in tiles.items():
        tileset = getAllOrientations(uid, tile)

        grid[y][x]["id"] = uid
        done = False
        for t in tileset:

            fitX, fitY = True, True
            if x - 1 >= 0:
                # does left corner fit
                compareY = grid[y][x-1]["tile"][:, 9]
                if not np.array_equal(compareY, t[:, 0]):
                    fitX = False
            if y - 1 >= 0:
                # does top corner fit
                compareY = grid[y-1][x]["tile"][9]
                if not np.array_equal(compareY, t[0]):
                    fitX = False

            if fitX and fitY:
                grid[y][x]["tile"] = t
                nextX = (x + 1) % cubelen
                nextY = y + int((x+1)/cubelen)

                newtiles = deepcopy(tiles)
                del newtiles[uid]
                # {x: d[x] for x in d if x not in keys}

                buildgrid(nextX, nextY, cubelen, grid, newtiles)
                done = True
                break
        if done:
            break


buildgrid(0, 0, dim, grid, tiles)

print("built grid!")

# remove borders from tiles

for y in grid:
    for x in y:
        x["tile"] = x["tile"][1:9, 1:9]

# generate merged image

lines = []
for y in grid:
    line = None
    for x in y:
        if line is None:
            line = x["tile"]
        else:
            line = np.concatenate((line, x["tile"]), 1)
    lines.append(line)

picture = None
for line in lines:
    if picture is None:
        picture = line
    else:
        picture = np.concatenate((picture, line), 0)

pictures = getAllOrientations("picture", picture)

print("counting monsters...")

# 00000000000000000010
# 10000110000110000111
# 01001001001001001000

monster = np.array(\
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]
    )
mon_width, mon_height = 3, 20
mon_active = 15

count = 0
waves = 0
for i in picture:
    for j in i:
        waves += j

monstercount = 0
for pic in pictures:
    count += 1
    for y in range(len(pic)-3):
        for x in range(len(pic)-20):
            if np.array_equal(np.multiply(monster, pic[y:y+mon_width, x:x+mon_height]), monster):
                monstercount += 1

print(waves - monstercount*mon_active)
print("done")
