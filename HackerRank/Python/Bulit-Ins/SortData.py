N, M = map(int, input().split())

# N-> ilosc wierszy
# M -> ilosc kolumn
# tablica -> macierz
# K - indeks po ktorym sortujemy

tablica = []
for i in range(N):
    tablica.append(list(map(int, input().split())))
K = int(input())

# wydruk czy dobrze input zapisany

# print(N)
# print(M)
# print(tablica)
# print(K)

# sortujemy, po kluczu -> indeksie K w każdym rzędzie

tablica.sort(key=lambda rzad: int(rzad[K]))

# czy dobrze posortowane
# print(tablica)

# wyswietlenie macierzy w "ichniejszym" wygladzie

for i in range(N):
    print(" ".join(map(str, tablica[i])))
