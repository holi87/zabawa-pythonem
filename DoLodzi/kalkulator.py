# Zadanie:
# Stwórz klasę kalkulator umożliwiającą dodawanie, odejmowanie, mnożenie oraz dzielenie.
# Po wprowadzeniu z klawiatury dwoch liczb rzeczywistych (X i Y) wydrukuje na ekranie informacje:
# Suma liczb X i Y to: tutaj suma
# Różnica liczb X i Y to: tutaj różnica
# Iloczyn liczb X i Y to: tutaj iloczyn
# Iloraz liczb X i Y to: tutaj iloraz
#


class Kalkulator:
    def __init__(self, liczba1, liczba2):
        self.pierwszaLiczba = liczba1
        self.drugaLiczba = liczba2

    def dodawanie(self):
        return self.pierwszaLiczba + self.drugaLiczba

    def odejmowanie(self):
        return self.pierwszaLiczba - self.drugaLiczba

    def mnozenie(self):
        return self.pierwszaLiczba * self.drugaLiczba

    def dzielenie(self):
        try:
            return self.pierwszaLiczba / self.drugaLiczba
        except ZeroDivisionError:
            return "druga liczba to 0, nie dzieli się przez zero"

try:
    wpis1 = float(input("wpisz liczbę: "))
    wpis2 = float(input("wpisz liczbę: "))

    testZera = Kalkulator(1, 0)
    testUjemnej = Kalkulator(43, -2)
    testUlamka = Kalkulator(0.5, 2)
    testKombinacyjny = Kalkulator(-0.25, 49.12)

    kalkus = Kalkulator(wpis1, wpis2)

    print(kalkus.dodawanie())

    assert testZera.dodawanie() == 1
    assert testUjemnej.dodawanie() == 41
    assert testUlamka.dodawanie() == 2.5
    assert testKombinacyjny.dodawanie() == (49.12-0.25)

    print(kalkus.odejmowanie())

    assert testZera.odejmowanie() == 1
    assert testUjemnej.odejmowanie() == 45
    assert testUlamka.odejmowanie() == -1.5
    assert testKombinacyjny.odejmowanie() == 49.37

    print(kalkus.mnozenie())

    assert testZera.mnozenie() == 0
    assert testUjemnej.mnozenie() == - 86
    assert testUlamka.mnozenie() == 1
    assert testKombinacyjny.mnozenie() == (49.12 * -0.25)

    print(kalkus.dzielenie())

    assert testZera.dzielenie() == "druga liczba to 0, nie dzieli się przez zero"
    assert testUjemnej.dzielenie() == (43/-2)
    assert testUlamka.dzielenie() == (0.5/2)
    assert testKombinacyjny.dzielenie() == (-0.25/49.12)

except ValueError:
    print("nie wpisano liczb")
