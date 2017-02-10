#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# your code goes here
a = sorted(a)

wynik = a[1]-a[0]
for i in range(2,n):
    wynik = min(wynik, a[i]-a[i-1])
print(wynik)