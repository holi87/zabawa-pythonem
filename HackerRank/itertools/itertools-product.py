from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(' '.join(str(i) for i in product(A, B)))
