# Program obliczający wynagrodzenie pracownika, uwzględniając możliwość otrzymania premii.
#
basic_salary = 5000  # Wynagrodzenie zasadnicze
total_salary = 0  # Całkowite wynagrodzenie
bonus_percentage = 0.30  # 30% premii
is_bonus = input('Czy pracownik otrzymuje premię? (Y/N): ').lower() == 'y'  # Sprawdzenie, czy pracownik otrzymuje premię

# Obliczanie całkowitego wynagrodzenia
if is_bonus:
    total_salary = basic_salary + (bonus_percentage * basic_salary)  # Wynagrodzenie z premią
else:
    total_salary = basic_salary  # Wynagrodzenie bez premii

# Wyświetlenie wyników
print(f'Wynagrodzenie zasadnicze: {basic_salary} zł')
print(f'Premia uwzględniona? {"Tak" if is_bonus else "Nie"}')
print(f'Całkowite wynagrodzenie: {total_salary} zł')
