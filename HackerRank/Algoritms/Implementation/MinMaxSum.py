#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
# moj kod ponizej
lista = [a, b, c, d, e]
print(sum(lista)-max(lista), sum(lista)-min(lista))
