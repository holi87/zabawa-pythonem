from turtle import *


def wielokat(iloscBokow = 4, dlugoscBoku = 100):
    for x in range(4):
        fd(dlugoscBoku)
        rt(360 // iloscBokow)

for i in range(10):
    wielokat(5, 30)
    rt(36)


sleep(5)