def factorial(liczba):
    wynik = 1
    for i in range(1,liczba+1):
        wynik *= i
    print(wynik)

factorial(int(input()))
