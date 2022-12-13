#! /usr/bin/env python3

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

# ==== SOLUTION ====

card_pk, door_pk = [int(row.strip()) for row in data.split('\n')[:-1]]

card_ls, door_ls = 0, 0
for loop in range(1000000):
    transformed = pow(7, loop, 20201227)
    if transformed == card_pk:
        card_ls = loop
        break

print(f"Card loop size: {card_ls}")
key = pow(door_pk, card_ls, 20201227)

print(key)

# output: 18608573
assert key == 18608573
