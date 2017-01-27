M = int(input())
pierwszySet = set(map(int, input().split()))
N = int(input())
drugiSet = set(map(int, input().split()))

#print(pierwszySet)
#print(drugiSet)

tempSet = pierwszySet.difference(drugiSet)
tempSet.update(drugiSet.difference(pierwszySet))
tempSet = sorted(tempSet)
#print(tempSet)
lista = list(tempSet)
#print(lista)
for i in lista:
    print(i)
