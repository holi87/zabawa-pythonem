# wczytuje pytanie ile masz lat:
# do 18 nie dorosły i powtórka

wiek = 0
while wiek < 18:
    wiek = int(input("Podaj ile masz lat: "))
    if 18 > wiek:
        print("nie jesteś dorosły ")
print("jesteś dorosły")

# ew zwykly while
