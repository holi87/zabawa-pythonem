# wersja pierwsza:
# def factorial(liczba):
#     wynik = 1
#     for i in range(1, liczba+1):
#         wynik *= i
#     print(wynik)
#
# factorial(int(input()))

# wersja wg zalozen HR


def factorial2(liczba2):
    for i in range(1, liczba2+1):
        if liczba2 == 2:
            return 2
        elif liczba2 == 1 or liczba2 == 0:
            return 1
        else:
            return factorial2(liczba2-1)*liczba2

print(factorial2(int(input())))
