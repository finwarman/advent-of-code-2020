#! /usr/bin/env python3
import re
import math
from functools import reduce

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

def subgame(deck1, deck2):
    played_rounds = set()
    # while len(deck1) > 0 and len(deck2) > 0:
    while deck1 and deck2:

        round_hash = str(deck1) + "_" + str(deck2)
        if round_hash in played_rounds:
            # return deck1, deck2
            return True if deck1 else False
        else:
            played_rounds.add(round_hash)

        p1 = deck1.pop()
        p2 = deck2.pop()

        # p1_win = False
        if len(deck1) >= p1 and len(deck2) >= p2:
            # p1_win, _ = subgame(deck1[-p1:], deck2[-p2:])
            p1_win = True if subgame(deck1[-p1:], deck2[-p2:]) else False
        else:
            p1_win = p1 > p2

        if p1_win:
            # deck1[:0] = [p2, p1]
            deck1 = [p2, p1] + deck1
            # deck1.insert(0, p1)
            # deck1.insert(0, p2)
        else:
            # deck2[:0] = [p1, p2]
            deck2 = [p1, p2] + deck2
            # deck2.insert(0, p2)
            # deck2.insert(0, p1)
    # return deck1, deck2
    return deck1


# rp1, rp2 = subgame(player1[::-1], player2[::-1])
# deck = rp1 + rp2

deck = subgame(player1[::-1], player2[::-1])
m = 0
for i in range(len(deck)):
    m += (i+1)*deck[i]
print(m)
