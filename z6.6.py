# Kalkulator opłaty parkingowej

godziny = int(input("Podaj liczbę godzin parkowania: "))

if godziny <= 2:
    oplata = 5
elif godziny <= 6:
    oplata = 15
else:
    oplata = 20

print(f"Opłata za parkowanie: {oplata} zł")
