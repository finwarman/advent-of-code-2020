#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('22.txt', 'r') as file:
    data = file.read().strip()

rows = [[row.strip() for row in tile.split('\n')] for tile in data.split('\n\n')]

# ==== SOLUTION ====
player1 = [int(x) for x in rows[0][1:]]
player2 = [int(x) for x in rows[1][1:]]

all_cards = set()
all_cards.update(player1)
all_cards.update(player2)
deck_size = len(all_cards)

# print(player1, deck_size)


while len(player1) > 0 and len(player2) > 0:
    p1 = player1.pop(0)
    p2 = player2.pop(0)

    top = max(p1, p2)
    bot = min(p1, p2)

    p = player1 if p1 > p2 else player2

    p.append(top)
    p.append(bot)


result_list = (player1 + player2)[::-1]
m = 0
for i in range(len(result_list)):
    m += (i+1)*result_list[i]
print(m)
