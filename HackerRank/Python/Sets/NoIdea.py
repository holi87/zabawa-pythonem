empLista = list(map(int, input().split()))
n = tempLista[0]
m = tempLista[1]
lista = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for i in lista:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)

# w sumie nie wiem czy nie powinno jeszcze sortowac listy
