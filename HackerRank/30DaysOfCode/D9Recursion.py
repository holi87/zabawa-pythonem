def factorial(liczba):
    wynik = 1
    for i in range(1,liczba+1):
        wynik *= i
    print(wynik)

factorial(int(input()))

# przerobić na:
# for i in range( 1, liczba+1):
#   if liczba = 2:
#       return 2
#   else:
#       return factorial(liczba-1) * liczba
#
#
#   print(factorial(int(input()))
