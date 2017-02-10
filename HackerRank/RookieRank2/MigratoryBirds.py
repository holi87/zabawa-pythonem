#!/bin/python3

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
tablica = [0, 0, 0, 0, 0]

for i in range(n):
    if types[i] == 1:
        tablica[0] += 1
    elif types[i] == 2:
        tablica[1] += 1
    elif types[i] == 3:
        tablica[2] += 1
    elif types[i] == 4:
        tablica[3] += 1
    else:
        tablica[4] += 1

wynik = tablica.index(max(tablica)) + 1

print(wynik)

# rozwiazanie beznadziejne, do przerobiena, ale dziala.
