#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
# moj kod:
# print(arr)
# sumaH = 0 - mozna schowac
tablicaSum = []
# [][] -> [0][0], [1][0], [2],[0], [1][1], [0][2],[1][2],[2][2] -> [0][0-2] + [1][1] + [2][0-2]
for j in range(4):
    for i in range(4):
        # poczatkowa wersja
        # sumaH = arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr [j+1][i+1] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]
        # tu ladniej zasiegowo
        # sumaH = sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3])
        # tablicaSum.append(sumaH)
        # a tu jeszcze wytniemy
        tablicaSum.append(sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3]))
print(max(tablicaSum))
