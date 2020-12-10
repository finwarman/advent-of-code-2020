#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('10.txt', 'r') as file:
    data = file.read().strip()

rows = sorted([int(row.strip()) for row in data.split('\n')])

# ==== SOLUTION ====

def getJoltageChain(jolts):
    dp = [0 for _ in range(len(jolts))]
    dp[0] = 1 # default number of combination is 1, for 0

    # for each previous value within [1,2,3] voltage range
    # current combination total = sum of previous totals where joltage within range
    for i in range(1, len(jolts)):
        for j in range(1, len(jolts)):
            diff = jolts[i] - jolts[i - j]
            if diff > 3 or i-j < 0:
                break
            dp[i] += dp[i - j]

    # print(dp)
    return dp[-1]

joltages = [0] + sorted(rows)
result = getJoltageChain(joltages)

print(result)
