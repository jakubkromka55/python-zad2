# Program sprawdzający, czy podany numer dnia miesiąca jest poprawny

month = int(input('Podaj numer miesiąca (1..12): '))
day = int(input('Podaj numer dnia miesiąca: '))
day_ok = False

# Sprawdzenie, czy dzień jest poprawny dla miesięcy z 31 dniami
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >= 1 and day <= 31:
        day_ok = True
# Sprawdzenie dla miesięcy z 30 dniami
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        day_ok = True
# Sprawdzenie dla lutego (28 dni)
elif month == 2:
    if day >= 1 and day <= 28:
        day_ok = True

# Komunikat w zależności od poprawności dnia
message = f'Dzień {day} dla miesiąca {month}'
if day_ok:
    print(f'{message} jest poprawny')
else:
    print(f'{message} jest niepoprawny')
