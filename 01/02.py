#! /usr/bin/env python3

data = ""
with open('01.txt', 'r') as file:
    data = file.read()

nums = sorted(list(set([int(x) for x in data.strip().split('\n') if int(x) <= 2020])))

for i in range(len(nums)-1, -1, -1):
    for numx in nums:
        y = numx + nums[i]
        if y > 2020 or numx == nums[i]:
            continue

        for numy in nums:
            x = numx + numy + nums[i]
            if x > 2020 or numy == nums[i] or numy == numx:
                continue
            if x == 2020:
                print(numx * numy * nums[i])
                quit()
