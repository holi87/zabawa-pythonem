from turtle import *

# pierwszy parametr = ilosc warstw (1-25)
# dlugosc boku ostatniego kwadrata (100-200)

# rysujemy od dołu
# rozbic na osobne funkcje - kwadrat, warstwy
# przeliczyc skad ma startowac zolw w kolejnej warstwie (wyliczyc z boku poprzedniego najlatwiej)
# kazda warstwa ma 1 kwadrat wiecej, wiec dlugosc boku / ilosckwadratow => warstwa = ilosc kwadratow
# punkt startowy cofnij o dlugoscPoczatkowa - dlugoscAktualna w poziomie

# funkcja pisząca rysująca pojedynczy kwadrat


def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)

# tu robimy z kwadratow warstwe zlozona z określonej ilości (iloscKwadratow)
# o okreslonym boku (dlugoscBoku)


def warstwa(iloscKwadratow, dlugoscBoku):
    narysowane = 0
    while narysowane < iloscKwadratow:
        if not narysowane == 0:
            fd(dlugoscBoku)
        kwadrat(dlugoscBoku)
        narysowane += 1

# tutaj łączymy kolejne warstwy według ilości warstw (ilosc) i długości boku pierwszego czyli dolnego kwadratu (dlogosc)


def warstwy(ilosc, dlugosc):
    aktualnaWarstwa = 1  # zmienna wskazująca pozycje którą warstwę aktualnie rysujemy
    aktualnaDlugosc = dlugosc  # zmienna pokazuje aktualną długość kwadratu który rysujemy
    while aktualnaWarstwa <= ilosc:

        # wywołujemy funkcje rysującą warstwe

        warstwa(aktualnaWarstwa, aktualnaDlugosc)

        # sprawdzamy czy jestesmy w ostatniej warstwie a jak nie to przesuwamy żółwia na pozycje startową kolejnej

        if not aktualnaWarstwa == ilosc:

            # odwracamy zolwia i kierujemy go na lewa krawedz rysunku

            rt(180)
            fd(dlugosc - aktualnaDlugosc)

            # liczymy długość boku kwadratów w kolejnej warstwie aby
            # żółwik skręcił w prawo i poszedł do pozycji z ktorej rysujemy nastepna warstwe

            nastepnaDlugosc = dlugosc / (aktualnaWarstwa + 1)
            rt(90)
            fd(nastepnaDlugosc)

            # ustawiamy pyszczek zolwia w dobrym kierunku by mogl rysowac nowa warstwe

            rt(90)

            # zmieniamy aktualna dlugosc boku aby wywolac w kolejnej zawijasie petli funkcje z nowym parametrem
            # jest pod instrukcja warunkowa aby nie zmieniac dlugosci w ostatniej iteracji gdy to jest zbedne

            aktualnaDlugosc = nastepnaDlugosc
        aktualnaWarstwa += 1


def dodatkoweUstawieina():
    title("Żółw według Grześka Holaka")
    ht()  # to chowa żółwia
    speed(0) # max prędkość rysowania

    # to tak aby zolw sie zmiescilo w razie max danych

    screensize(400, 1000)
    penup()
    sety(-240)
    pendown()

dodatkoweUstawieina()
warstwy(25, 200)

# wychodzimy po kliknieciu


exitonclick()
