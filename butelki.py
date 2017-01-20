zwykla = 0
pytanie = "Czy chcesz dodać jeszcze jakieś butelki?"
odpowiedz = "n"
while odpowiedz == "t" or odpowiedz == "tak":
    print("odpowiedź: tak")
    zwykla += int(input("Wpisz ile butelek dodać: "))
    print(pytanie)
    odpowiedz = input()

print("liczba butelek to: %d" % zwykla)
