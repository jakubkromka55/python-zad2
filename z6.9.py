# Sprawdzanie, czy podane imię to polskie imię żeńskie

imie = input("Podaj imię: ")

if imie.endswith("a"):
    print(f"{imie} polskie imię żeńskie")
else:
    print(f"{imie} to nie jest polskie imię żeńskie")
