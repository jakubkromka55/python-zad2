# Klasyfikacja według grupy wiekowej

wiek = int(input("Podaj swój wiek: "))

if wiek < 13:
    print("Dziecko")
elif wiek <= 19:
    print("Nastolatek")
elif wiek <= 64:
    print("Dorosły")
else:
    print("Senior")
