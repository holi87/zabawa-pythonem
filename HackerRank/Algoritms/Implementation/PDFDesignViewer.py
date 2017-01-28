#!/bin/python3

import sys


h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
# zrobmy liste liter w alfabecie, przydaloby sie to latwiej generowac
litery = [i for i in "abcdefghijklmnopqrstuvwxyz"]
# print(litery)
# zrobmy slownik gdzie klucz to litera a value to wysokosc dlatego najpierw zipujemy 2 listy
# a potem robimy z list krotek slownik
slownik = dict(zip(litery,h))
# najwyzsza litere w slowie obliczmay szukajac max value po kluczu w slowie bo kluczem sa litery
najwyzsza = max ( slownik[i] for i in word)
# wysokosc = dlugosc slowa (kazda litera ma szerokosc 1 wiec do mnozenia mozna pominac, liczy sie liczba liter)
# razy najwyzsza litera wystepujaca w slowniku
wysokosc = len(word) * najwyzsza
print(wysokosc)
