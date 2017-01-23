t = int(input())

for i in range(t):
    tekst = input()
    parz = ""
    niep = ""
    for j in range(len(tekst)):
        if j % 2 == 0:
            parz += tekst[j]
        else:
            niep += tekst[j]
    print("%s %s" % (parz, niep))
