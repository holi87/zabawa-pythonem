#!/bin/python3

import sys

import re
s = input().strip()
wzorzec = r"[A-Z]"
duze = re.findall(wzorzec, s)
print(len(duze)+1)
