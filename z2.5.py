# Program obliczający i drukujący kwartał roku dla danego numeru miesiąca (1..12)

month = int(input('Podaj numer miesiąca (1..12): '))

# Określenie kwartału na podstawie numeru miesiąca
if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

# Wyświetlenie wyniku
print(f'Miesiąc {month} należy do kwartału {quarter}')
