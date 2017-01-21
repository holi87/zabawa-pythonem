cube = lambda x: x ** 3  # complete the lambda function


def listaCiaguFibonacciego(n):
    if n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return listaCiaguFibonacciego(n - 1) + listaCiaguFibonacciego(n - 2)


def fibonacci(n):
    lista = []
    for i in range(n):
        lista.append(listaCiaguFibonacciego(i))

    return lista

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))  # blad z braku przelistowania mapy?
