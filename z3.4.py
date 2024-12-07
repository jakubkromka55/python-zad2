# Program sprawdzający, czy przynajmniej jedna liczba nie jest ujemna

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))

# Sprawdzamy, czy przynajmniej jedna z liczb nie jest ujemna
if not x < 0 or not y < 0:
    print(f'Przynajmniej jedna z liczb {x} i {y} nie jest ujemna')
else:
    print(f'Obie liczby {x} i {y} są ujemne')
