#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

iloscDodatnich = 0
iloscUjemnych = 0
iloscZer = 0
for i in range(n):
    if arr[i] == 0:
        iloscZer += 1
    elif arr[i] < 0:
        iloscUjemnych += 1
    else:
        iloscDodatnich += 1

print("%.6f" % (iloscDodatnich/n))
print("%.6f" % (iloscUjemnych/n))
print("%.6f" % (iloscZer/n))