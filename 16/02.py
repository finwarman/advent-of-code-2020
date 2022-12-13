#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('16.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====
limits = []

rowslim = 20
# rowslim = 3

otherslim = 25
# otherslim = 8

ticket_types = {}

for row in rows[:rowslim]:
    name = row[:row.find(': ')]
    row = row[row.find(': ')+2:]
    split = row.split(" ")

    la1, la2 = split[0].split("-")
    limits.append(  (int(la1), int(la2))  )

    lb1, lb2 = split[2].split("-")
    limits.append(  (int(lb1), int(lb2))  )

    ticket_types[name] = [(int(la1), int(la2)), (int(lb1), int(lb2))]


valid_tickets = []

for row in rows[otherslim:]:
    valid = True
    for val in row.split(","):
        val = int(val)
        valid = False
        for pair in limits:
            if (pair[0] <= val <= pair[1]):
                valid = True
                break
        if not valid:
            break
    if valid:
        valid_tickets.append([int(x) for x in row.split(",")])

results = {}
finished_i = set()

while len(results.keys()) < len(ticket_types.keys()):
    for i in range(len(valid_tickets[0])):
        if i in finished_i:
            continue
        potential = set(ticket_types.keys())
        for ticket in valid_tickets:
            val = ticket[i]
            new_pots = potential.copy()
            for name in potential:
                pairs = ticket_types[name]
                if (name in results) or ((not(pairs[0][0] <= val <= pairs[0][1]) and not(pairs[1][0] <= val <= pairs[1][1]))):
                    new_pots.discard(name)
            potential = new_pots

        if len(potential) == 1:
            finished_i.add(i)
            results[min(potential)] = i

print()

myticket = [int(x) for x in rows[22].split(",")]
result = 1
for key in results.keys():
    print("{:>20}: {}".format(key, results[key]))
    if "departure" in key:
        result *= myticket[results[key]]

print()
print(result)
print()
