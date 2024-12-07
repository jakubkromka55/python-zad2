# Sprawdzanie, czy liczba wpisana z klawiatury jest parzysta, czy nieparzysta
#
number = int(input('Podaj liczbę: '))  # Pobranie liczby od użytkownika

# Sprawdzenie, czy liczba jest parzysta
if number % 2 == 0:
    print(f'{number} jest liczbą parzystą')  # Komunikat dla liczby parzystej
else:
    print(f'{number} jest liczbą nieparzystą')  # Komunikat dla liczby nieparzystej
