# Program obliczający liczbę dni w danym miesiącu

month = int(input('Podaj numer miesiąca (1..12): '))

# Sprawdzenie liczby dni w miesiącu
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31  # Miesiące z 31 dniami
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30  # Miesiące z 30 dniami
else:
    days = 28  # Luty zawsze ma 28 dni

# Drukowanie wyniku
print(f'Miesiąc {month} ma {days} dni')
