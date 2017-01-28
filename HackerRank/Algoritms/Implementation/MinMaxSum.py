#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
# moj kod ponizej
# lista = [a, b, c, d, e]
print(sum(a, b, c, d, e)-max(a, b, c, d, e), sum(a, b, c, d, e)-min(a, b, c, d, e))
