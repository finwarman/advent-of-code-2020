#! /usr/bin/env python3

data = ""
with open('01.txt', 'r') as file:
    data = file.read()

nums = sorted(list(set([int(x) for x in data.strip().split('\n') if int(x) <= 2020])))

for i in range(len(nums)-1, -1, -1):
    for num in nums:
        x = num + nums[i]
        if x == 2020:
            print(num * nums[i])
            quit()
        if x > 2020:
            continue

# N.B. Can be done in O(n) by adding to a set and simply checking if 2020-n exists in that set,
#    while adding from the input file
