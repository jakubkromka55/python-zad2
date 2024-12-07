# Zniżka przysługuje dzieciom poniżej 18 roku życia lub osobom w wieku 65 lat i starszym.

age = int(input('Podaj swój wiek: '))

# Sprawdzenie, czy osoba kwalifikuje się do zniżki
if age < 18 or age >= 65:
    print('Przysługuje Ci zniżka')
else:
    print('Nie przysługuje Ci zniżka')
