#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('20.txt', 'r') as file:
    data = file.read().strip()

tiles = [[row.strip() for row in tile.split('\n')] for tile in data.split('\n\n')]

# ==== SOLUTION ====

def get_borders(tile):
    width, height = len(tile[0]), len(tile)

    borders = []
    borders.append(tile[0])
    borders.append(tile[-1])
    l, r = "", ""
    for i in range(height):
        l += tile[i][0]
        r += tile[i][-1]
    borders.append(l)
    borders.append(r)

    # TOP, BOTTOM, LEFT, RIGHT
    return borders


borders = {}

for tile in tiles:
    uid = int(''.join(tile[0][5:-1]))
    pixels = tile[1:]

    border_set = get_borders(pixels)

    borders[uid] = border_set


id_matches = {}

for uid in borders.keys():
    matches = {}

    # TOP, BOTTOM, LEFT, RIGHT (FTOP, FBOTTOM, FLEFT, FRIGHT)
    edges = borders[uid]
    edges.extend([s[::-1] for s in edges])

    matches = {}
    for i in range(len(edges)):
        matches[i] = []

    for nuid in borders.keys():
        if nuid == uid:
            continue

        nedges = set(borders[nuid])
        for i in range(len(edges)):
            edge = edges[i]
            if edge in nedges:
                matches[i].append(nuid)

    print(uid, matches)
    id_matches[uid] = matches



print()
corners = []
for uid in id_matches.keys():
    options = id_matches[uid]
    pids = set()
    for i in range(len(options.keys())):
        xids = options[i]
        for x in xids:
            pids.add(x)
    if len(pids) == 2:
        corners.append(uid)
    # print(uid, pids)

print(corners)
print(len(corners))
m = 1
for x in corners:
    m = m * x
print()
print(m)
