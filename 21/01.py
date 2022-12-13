#! /usr/bin/env python3
import re
import math
from collections import defaultdict

# ==== INPUT ====
data = ""
with open('21.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

# ==== SOLUTION ====

all_allergens = defaultdict(int)
all_ingredients = defaultdict(int)
foods = []

for row in rows:
    parts = row.split(" (contains ")
    ingredients = parts[0].split(" ")
    allergens = parts[1][:-1].split(", ")

    for a in allergens:
        all_allergens[a] += 1

    for i in ingredients:
        all_ingredients[i] += 1

    foods.append({"ingredients": set(ingredients), "allergens": set(allergens)})

allergen_candidates = {}

for allergen in all_allergens.keys():
    for food in foods:
        f_ingr = food["ingredients"]
        f_allr = food["allergens"]

        if allergen in f_allr:
            if allergen not in allergen_candidates:
                allergen_candidates[allergen] = set()
                for i in f_ingr:
                    allergen_candidates[allergen].add(i)
            else:
                for i in all_ingredients.keys():
                    if i not in f_ingr:
                        allergen_candidates[allergen].discard(i)

flagged_as_allergen = set()

for cand in allergen_candidates.keys():
    for a in allergen_candidates[cand]:
        flagged_as_allergen.add(a)
    print(cand, allergen_candidates[cand])
    print()

print(flagged_as_allergen)

flagged_as_safe = set()

tot = 0
for ing in all_ingredients.keys():
    if ing in flagged_as_allergen:
        continue
    else:
        flagged_as_safe.add(i)
        tot += all_ingredients[ing]
print(tot)

print(flagged_as_safe)
