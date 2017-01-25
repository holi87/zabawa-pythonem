ilosc = int(input())
phoneBook = {} # słownik, klucz: wartosc, kluczem bedzie imie bo po nim szukamy
# wypelnianie slownika
for i in range(ilosc):
    imie, numer = input().split()
    numer = int(numer)
    # sprawdzenie czy poprawne wpisy
    # print(imie)
    # print(numer)
    phoneBook[imie] = numer
# sprawdzenie czy poprawnie wpisalem w slownik
# print(phoneBook)
# przeszukiwanie slownika
for i in range(ilosc):
    imieSzukane = input()
    if imieSzukane in phoneBook:
        print("%s=%d" % (imieSzukane, phoneBook[imieSzukane]))
    else:
        print("Not found")
