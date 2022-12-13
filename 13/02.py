#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('13.txt', 'r') as file:
    data = file.read().strip()

rows = data.split('\n')
buses = []
i = 0
for bus in rows[1].split(","):
    if bus == "x":
        i += 1
        continue
    buses.append((int(bus), i))
    i += 1

print(buses)

# ==== SOLUTION ====

# using chinese remainder theorem;
# see https://brilliant.org/wiki/chinese-remainder-theorem/

# N = product of all ids ('coprimes')
product = 1
for time, diff in buses:
    product *= time

# modular inverse:  pow(b, -1, mod=m) calculates inverse of b mod m, aka.
# finding some number d such that d * b % m = 1

total = 0
for n_i, diff in buses:
    # n_hat_i = N // n_i
    y_i = product // n_i

    # modular inverse of n_hat, modulo n_i
    z_i = pow(y_i, -1, n_i)

    a_i = (n_i - diff)
    total += a_i * y_i * z_i

ch_remainder = total % product

print()
# print(total)
print(ch_remainder)
