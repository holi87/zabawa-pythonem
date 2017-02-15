#!/bin/python3

import sys
import re

N = int(input().strip())
tablicaImion = []
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    if re.match(".+@gmail\.com$", emailID) is not None:
        tablicaImion.append(firstName)

for i in sorted(tablicaImion):
    print(i)
