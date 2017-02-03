class Difference:
    def __init__(self, a):
        self.__elements = a

# poczatek mojego kodu


    def computeDifference(self):
        najwieksza = max(self.__elements)
        najmniejsza = min(self.__elements)
        self.maximumDifference = abs(najmniejsza-najwieksza)

# koniec mojego kodu
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)