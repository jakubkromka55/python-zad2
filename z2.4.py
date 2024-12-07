# Program prosi o wprowadzenie symbolu operacji matematycznej (+, -, *, /) i dwóch liczb.

# Pobranie danych od użytkownika
number1 = float(input('Podaj pierwszą liczbę: '))
number2 = float(input('Podaj drugą liczbę: '))
operator = input('Podaj operator matematyczny (+, -, *, /): ').strip()

# Wykonanie operacji matematycznej
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:  # Sprawdzenie dzielenia przez zero
        result = number1 / number2
    else:
        result = 'Błąd: Dzielenie przez zero!'
else:
    result = 'Błąd: Nieprawidłowy operator!'

# Wyświetlenie wyniku
print(f'{number1} {operator} {number2} = {result}')
