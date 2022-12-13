#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
# with open('19.txt', 'r') as file:
with open('1902.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip() for row in data.split('\n')]

spliti = rows.index('')
ruleslist = rows[:spliti]
strings= rows[spliti+1:]

# ==== SOLUTION ====
print(ruleslist)
print()
print(strings)


rules = {}

for rule in ruleslist:
    i = rule.index(':')
    num = rule[:i]
    body = rule[i+2:]
    # print(num, "|", body)

    rules[num] = body.strip('"')

def parse_rules(rule_id):
    # print(rule_id)
    if rule_id in "ab|":
        return rule_id
    sub_rules = rules[rule_id].split(' ')
    if rule_id in sub_rules:
        if len(sub_rules) == 4:
            return "" + parse_rules(sub_rules[0]) + "+"
        if len(sub_rules) == 6:
            generated_rules = []
            for i in range(1, 5):  # Handling only 5 depths of recursion for speed - dataset only goes this deep
                generated_rules.append(f"({parse_rules(sub_rules[0])}{{{i}}}{parse_rules(sub_rules[1])}{{{i}}})")
            return "(" + '|'.join(generated_rules) + ")"
    new_rules = ''.join([parse_rules(x) for x in sub_rules])
    return new_rules if len(new_rules) == 1 or "|" not in new_rules else \
        "(" + ''.join([parse_rules(x) for x in sub_rules]) + ")"


print("^" + parse_rules("0") + "$")
all_rules = re.compile("^" + parse_rules("0") + "$")
total = 0
for message in strings:
    print(message, all_rules.match(message))
    if all_rules.match(message):
        total += 1
print(f"Part 1 total: {total}")
