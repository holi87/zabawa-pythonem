#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sumaPrzekatna = 0
sumaPrzeciw = 0

for i in range(n):
    sumaPrzekatna += a[i][i]
    sumaPrzeciw += a[i][n-i-1]

# print (sumaPrzekatna)
# print (sumaPrzeciw)

roznica = abs(sumaPrzekatna-sumaPrzeciw)
print(roznica)
