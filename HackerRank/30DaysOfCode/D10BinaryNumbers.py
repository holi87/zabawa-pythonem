#!/bin/python3

import sys


n = int(input().strip())
binarny = bin(n)[2:]
# sprawdzenie czy wyrzucilem 0b
# print(binarny)
# split po zerach by je usunac

bezZer = binarny.split("0")
# print(bezZer)
# sprawdzenie dlugosci elementow w calej tablicy, aby znalezc najdluzszy
temp = 0
for i in range(len(bezZer)):
    if len(bezZer[i]) > temp:
        temp = len(bezZer[i])
print(temp)
