# Program sprawdzający, czy liczba jest dodatnia, ujemna, czy wynosi 0

number = int(input('Podaj liczbę: '))

# Sprawdzanie, czy liczba jest dodatnia, ujemna, czy równa zeru
if number > 0:
    print(f'Liczba {number} jest dodatnia')
elif number < 0:
    print(f'Liczba {number} jest ujemna')
else:
    print('Liczba wynosi 0')
