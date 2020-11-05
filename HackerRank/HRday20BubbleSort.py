#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalswap = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
            totalswap += 1
    if swaps == 0:
        break

print("Array is sorted in {} swaps.".format(totalswap))
print("First Element:", a[0])
print("Last Element:", a[n-1])
