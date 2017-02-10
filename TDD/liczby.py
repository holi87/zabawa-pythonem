def dodawanie(liczba1, liczba2):
    return liczba1 + liczba2


def dzielenie(liczba1, liczba2):
    try:
        return liczba1 / liczba2
    except ZeroDivisionError:
        return None


def mnozenie(liczba1, liczba2):
    return liczba1 * liczba2

