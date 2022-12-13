#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('23.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')]
cups = [int(x) for x in list(rows[0])]

# ==== SOLUTION ====

cups = cups + [i for i in range(10, 1000000+1)]

l = len(cups)

# dic = [0 for _ in range(l+1)]

dic = {}
# 1-indexed
for i in range(l-1):
    dic[cups[i]] = cups[i+1]
dic[cups[-1]] = cups[0]

current_label = dic[cups[-1]]

for i in range(0, 10000000):
    picked_up = []

    pick_up = current_label
    for j in range(3):
        pick_up = dic[pick_up]
        picked_up.append(pick_up)

    dest_label = current_label

    dest_label -= 1
    while dest_label in picked_up or dest_label <= 0:
        if dest_label <= 0:
            dest_label = l
        if dest_label in picked_up:
            dest_label -= 1

    temp = dic[picked_up[-1]]
    dic[picked_up[-1]] = dic[dest_label]
    dic[dest_label] = picked_up[0]
    dic[current_label] = temp

    current_label = temp # thank you /u/setapoux/

x = dic[1]
y = dic[x]
print(x, y, "\n" + str((x*y)))
