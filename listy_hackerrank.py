if __name__ == '__main__':
    N = int(input())
    lista = []
    for i in range(N):
        starter = input().split()
        if starter[0] == "insert":
            lista.insert(int(starter[1]), int(starter[2]))
        elif starter[0] == "remove":
            lista.remove(int(starter[1]))
        elif starter[0] == "append":
            lista.append(int(starter[1]))
        elif starter[0] == "sort":
            lista.sort()
        elif starter[0] == "pop":
            lista.pop()
        elif starter[0] == "reverse":
            lista.reverse()
        elif starter[0] == "print":
            print(lista)
