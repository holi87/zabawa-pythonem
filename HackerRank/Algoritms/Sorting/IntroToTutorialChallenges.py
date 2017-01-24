V = int(input())
n = int(input())
tablica = list(map(int, input().split()))

# test wartości

# print(V)
# print(n)
# print(tablica)

# algorytm wlasciwy

for i in range(n):
    if tablica[i] == V:
        print(i)
