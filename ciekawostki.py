# pozbycie sie konca linii z printa


print("tekst", end="KONIEC PRINTA")
print("")
print("tekst", end="")

# pozbycie sie znaku konca lini z wczytanego pliku - dobre na duze pliki bo dziala linijka po linijce

s = plik.readline().strip()
while s:
    print(s)
    s = plik.readline().strip()

#  random.org - do losowych liczb

