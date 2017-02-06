#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

liczbaPrzestawien = 0
for i in range(n):
    czyPosortowane = True
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            liczbaPrzestawien += 1
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            czyPosortowane = False
    if czyPosortowane:
        break

print("Array is sorted in %d swaps." % liczbaPrzestawien)
print("First Element: %d" % a[0])
print("Last Element: %d" % a[n - 1])
